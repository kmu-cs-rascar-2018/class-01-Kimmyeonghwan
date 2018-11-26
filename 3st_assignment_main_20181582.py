from SEN040134 import SEN040134_Tracking as Tracking_Sensor
# import Tracking sensor module(time module included)
from SR02 import SR02_Ultrasonic as Ultrasonic_Sensor
import time
import RPi.GPIO as GPIO
import rear_wheels
import front_wheels




if __name__ == "__main__":
    Tracker = Tracking_Sensor.SEN040134_Tracking([16, 18, 22, 40, 32])
    direction_controller = front_wheels.Front_Wheels(db='config')
    driving_controller = rear_wheels.Rear_Wheels(db='config')
    distance_detector = Ultrasonic_Sensor.Ultrasonic_Avoidance(35)
    angle = [-35, -30, -10, -5, 5, 10, 30, 35]
    speed = [35, 40, 50]  # 0 = 30, 1 = 40, 2= 50
    re = 0
    behind = 0
    
    try:
        while (re < 2):
            distance = distance_detector.get_distance()
            
            # 장애물이 있을 경우
            if distance < 20 and distance != -1:
                direction_controller.turn(90 + angle[0])  # 좌회전
                driving_controller.forward_with_speed(speed[0])
                time.sleep(1)
                while (Tracker.is_in_line == False):
                    direction_controller.turn(90 + angle[0])
                    #driving_controller.forward_with_speed(speed[0])
                direction_controller.turn(90 + angle[7])
                driving_controller.forward_with_speed(speed[0])
                time.sleep(1)
                while (Tracker.is_in_line == False):
                    direction_controller.turn(90 + angle[7])
                    driving_controller.forward_with_speed(speed[0])
            else:
                    
                # 급격하게 좌회전
                if Tracker.is_equal_status([1, 0, 0, 0, 0]):
                    direction_controller.turn(90 + angle[0])
                    driving_controller.forward_with_speed(speed[0])
                    behind = angle[0]

                # 좌회전
                elif Tracker.is_equal_status([1, 1, 0, 0, 0]):
                    direction_controller.turn(90 + angle[1])
                    driving_controller.forward_with_speed(speed[0])
                    behind = angle[1]

                # 조금 좌회전
                elif Tracker.is_equal_status([0, 1, 0, 0, 0]):
                    direction_controller.turn(90 + angle[2])
                    driving_controller.forward_with_speed(speed[1])
                    behind = angle[2]

                # 진짜 조금 좌회전
                elif Tracker.is_equal_status([0, 1, 1, 0, 0]):
                    direction_controller.turn(90 + angle[3])
                    driving_controller.forward_with_speed(speed[1])
                    behind = angle[3]

                # 직진
                elif Tracker.is_equal_status([0, 0, 1, 0, 0]):
                    direction_controller.turn(90)
                    driving_controller.forward_with_speed(speed[1])
                    behind = 0

                # 진짜 조금 우회전
                elif Tracker.is_equal_status([0, 0, 1, 1, 0]):
                    direction_controller.turn(90 + angle[4])
                    driving_controller.forward_with_speed(speed[1])
                    behind = angle[4]

                # 조금 우회전
                elif Tracker.is_equal_status([0, 0, 0, 1, 0]):
                    direction_controller.turn(90 + angle[5])
                    driving_controller.forward_with_speed(speed[1])
                    behind = angle[5]
                
                # 우회전
                elif Tracker.is_equal_status([0, 0, 0, 1, 1]):
                    direction_controller.turn(90 + angle[6])
                    driving_controller.forward_with_speed(speed[0])
                    behind = angle[6]

                # 많이 우회전
                elif Tracker.is_equal_status([0, 0, 0, 0, 1]):
                    direction_controller.turn(90 + angle[7])
                    driving_controller.forward_with_speed(speed[0])
                    behind = angle[7]

                elif Tracker.is_equal_status([0, 0, 0, 0, 0]):
                    direction_controller.turn(90 - behind)
                    driving_controller.backward_with_speed(speed[0])
                    time.sleep(0.1)
                

                if Tracker.is_equal_status([1, 1, 1, 1, 1]):
                    re += 1
                    driving_controller.forward_with_speed(speed[1])
                    time.sleep(1)
            
    
        #direction_controller.turn_straight()
        #driving_controller.stop(),
        #driving_controller.power_down()            
    except KeyboardInterrupt:
        GPIO.cleanup()
