import cv2
import time
from datetime import datetime
import numpy as np
import sounddevice as sd
from ultralytics import YOLO
from playsound import playsound
import csv

test_sound = True

stop_flag = False

# initialize mpl plot
#plt.ion()


# Load the model
model = YOLO('yolov8n.pt')


# THIS MUST BE CHANGED BY SUBJECT
height = 188 # cm
width = 41 # cm; shoulder width
leeway = 1 # high is less response, low is more response. 1.1 is 10% more fall per fall, 0.9 is 10% less fall per fall
path_to_sound_file = 'O.O'

fps_limit = 3
frame_storage_length = 10 # in seconds

time_stamps = np.ones(frame_storage_length * fps_limit) * datetime.now().timestamp()
heights = None
y_velocities = np.zeros(frame_storage_length * fps_limit)
y_accelerations = np.zeros(frame_storage_length * fps_limit)

# THIS MUST BE CHANGED WHEN FPS CHANGES
threshold = 200 * leeway


# audio sound detection setup
def audio_callback(indata, frames, time, status):
	global sound_level
	global sound_test
	global sounds
	
	sound_level = np.linalg.norm(indata) * 10
	sounds = np.append(sounds[datetime.now().timestamp() - sounds[:, 1] <= sound_storage_length], [[sound_level - sounds[-1, 0], datetime.now().timestamp()]], axis = 0)

sound_level = 0

sound_storage_length = 2 # in seconds
sounds = np.array([[-1, -1]])


time_grounded = 3
grounded_threshold = 0.5



class MoreThanOnePerson(Exception):
	pass


# main loop
def main():
	global stop_flag
	global test_sound
	global model
	global cap
	global height
	global width
	global leeway
	global fps_limit
	global frame_storage_length
	global time_stamps
	global heights
	global y_velocities
	global y_accelerations
	global threshold
	global sound_level
	global sound_storage_length
	global sounds
	global time_grounded
	global grounded_threshold
	global stream
	global fall_history

	stream = sd.InputStream(callback=audio_callback)
	cap = cv2.VideoCapture(0)

	fall_history_file = open(r'F:\Documents\HKAGE\AI and Big Data Analysis (Phase III) (A4AIG003C)\Pose_Detection_project\FallHistory.csv','a')  # time of each fall
	writer = csv.writer(fall_history_file)

	with stream:
		while cap.isOpened() and not stop_flag:
			# test #1
			if y_accelerations[-1] > threshold:
				# test #2
				time.sleep(1)
				if np.max(sounds[:, 0]) > 10 or not test_sound:
					# test #3
					time.sleep(time_grounded - 1)
					_, frame = cap.read()
					results = model.predict(source=frame, verbose=False)[0]
					results = results[results.boxes.cls == 0][0]
					boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in results.boxes.xywh])

					for box in boxes:
						pixel_width = box[2] - box[0]
						pixel_height = box[3] - box[1]

						scale = np.sqrt(width**2 + height**2)/np.sqrt(pixel_width**2 + pixel_height**2)
						scaled_height = pixel_height*scale

						if scaled_height < height * grounded_threshold:
							fall_time = datetime.now()
							writer.writerow([fall_time.year, fall_time.month, fall_time.day, fall_time.hour, fall_time.minute,fall_time.second])
							print("Fall!")
							playsound(path_to_sound_file)

			t0 = datetime.now().timestamp()
			
			_, frame = cap.read()
			results = model.predict(source=frame, verbose=False)[0]
			results = results[results.boxes.cls == 0][0]
			boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in results.boxes.xywh])

			# annotate and display video
			result = results.plot()
			
			cv2.imshow('output', result)

			try:
				if len(boxes) > 1:
					raise MoreThanOnePerson

				for box in boxes:
					pixel_width = box[2] - box[0]
					pixel_height = box[3] - box[1]

					scale = np.sqrt(width**2 + height**2)/np.sqrt(pixel_width**2 + pixel_height**2)

					#print(f"\nscale: {scale} || height: {pixel_height*scale}, {pixel_height} || width: {pixel_width*scale}, {pixel_width}")

					scaled_height = pixel_height*scale

					time_stamps = np.append(time_stamps[1::], [datetime.now().timestamp()])
					
					if type(heights) == type(None):
						heights = np.ones(frame_storage_length * fps_limit) * scaled_height
					heights = np.append(heights[1::], [scaled_height])
					
					y_velocities = np.append(y_velocities[1::], [(heights[-1] - heights[-2])/(time_stamps[-1] - time_stamps[-2])])
					y_accelerations = np.append(y_accelerations[1::], [(y_velocities[-1] - y_velocities[-2])/(time_stamps[-1] - time_stamps[-2])])

					#print(f"delta time: {time_stamps[-1] - time_stamps[-2]}, height: {heights[-1]}, vel: {y_velocities[-1]}, acc: {y_accelerations[-1]}")


			except MoreThanOnePerson:
				if datetime.now().timestamp() - t0 < 1/fps_limit:
					time.sleep(1/fps_limit - (datetime.now().timestamp() - t0)) #limit fps to fps_limit

			except AttributeError:
				if datetime.now().timestamp() - t0 < 1/fps_limit:
					time.sleep(1/fps_limit - (datetime.now().timestamp() - t0)) #limit fps to fps_limit

			#create a line plot(connect points with lines) with the x list as the x values and the y list as the y values
			'''if y_accelerations[-1] > threshold:
				plt.plot(time_stamps[-2::], y_accelerations[-2::], 'r')
			else: 
				plt.plot(time_stamps[-2::], y_accelerations[-2::], 'k')'''

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

			if datetime.now().timestamp() - t0 < 1/fps_limit:
				time.sleep(1/fps_limit - (datetime.now().timestamp() - t0)) #limit fps to fps_limit


	# stop the recording
	stream.close()
	cap.release()
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	fall_history_file.close()

def get_fall_hist(folder_path):
	with open(rf'{folder_path}FallHistory.csv') as file_obj:
		heading = next(file_obj)
		reader_obj = csv.reader(file_obj)
		result = np.array([[-1, -1, -1, -1, -1, -1]])
		for row in reader_obj:
			if len(row) != 0:
				result = np.append(result, [row], axis = 0)
		result = result[1::]
		return result

def clear_fall_hist(folder_path):
	with open(rf'{folder_path}FallHistory.csv', 'w') as file_obj:
		writer = csv.writer(file_obj)
		writer.writerow(['year','month','day','hour','minute','second'])