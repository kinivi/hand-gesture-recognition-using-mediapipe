from infrastructure.model.Labels import KeyPointLabel, PointHistoryLabel
from infrastructure.openCV.draw.draw_debug_messages import draw_bounding_rectangle, draw_info_text, \
    calculate_bounding_rectangle, \
    draw_point_history, draw_statistics
from infrastructure.openCV.draw.draw_hand_landmarks import draw_landmarks
import cv2 as cv

from infrastructure.openCV.video_capture.video_capture_lifecycle import Image


def draw_overlays_with_landmarks(image: Image, hand_sign_id, handedness, landmark_list,
                                 most_common_fg_id,
                                 hand_landmarks) -> Image:
    bounding_rectangle = calculate_bounding_rectangle(image, hand_landmarks)

    image_with_rectangle = draw_bounding_rectangle(image.image, bounding_rectangle)
    image_with_landmarks = draw_landmarks(image_with_rectangle, landmark_list)
    image_with_info = draw_info_text(
        image_with_landmarks,
        bounding_rectangle,
        handedness,
        KeyPointLabel(hand_sign_id).name,
        PointHistoryLabel(most_common_fg_id[0][0]).name,
    )
    return Image(image_with_info)


def draw_overlays(image: Image, fps, mode, number, point_history):
    image_with_point_history = draw_point_history(image.image, point_history)
    image_with_statistics = draw_statistics(image_with_point_history, fps, mode, number)
    return Image(image_with_statistics)
