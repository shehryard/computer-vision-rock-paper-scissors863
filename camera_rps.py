import cv2
import numpy as np
from keras.models import load_model
import time
import random

def get_prediction(model, image):
    
    resized_image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    normalized_image = (resized_image.astype(np.float32) / 127.0) - 1  # normalise the image
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image

    # Get model predictions
    predictions = model.predict(data)
    
    class_names = ["Rock", "Paper", "Scissors", "Nothing"]
    predicted_class_index = np.argmax(predictions[0])
    predicted_class = class_names[predicted_class_index]
    confidence = predictions[0][predicted_class_index]

    print(f"The model predicts: {predicted_class} with confidence: {confidence}")
    return predicted_class

def countdown(timer):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        remaining_time = max(0, timer - int(elapsed_time))
        print(f"Capture in {remaining_time} seconds...", end='\r')
        if elapsed_time >= timer:
            print("\nCapturing your hand gesture...")  # Replace with your desired action after the countdown
            break

def play_round():
    model = load_model('converted_keras/keras_model.h5')
    cap = cv2.VideoCapture(0)
    countdown_time = 3  # Adjust the countdown time as needed
    countdown(countdown_time)
    ret, frame = cap.read()

    cv2.imshow('captured_frame', frame) # Display the frame and predicted user guess
    # After the loop release the cap object
    cap.release()
    # Wait before window is closed to see the image
    cv2.waitKey(2000)
    # Destroy all the windows
    cv2.destroyAllWindows()
    
    user_guess = get_prediction(model, frame)  # Get the model prediction for the captured frame

    # Randomly pick an option for the computer
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)

    print(f"You chose: {user_guess}")
    print(f"Computer chose: {computer_choice}")

    # see who wins between computer and user
    if computer_choice == user_guess: 
        return "It is a tie!"
    elif (
        (computer_choice == "Rock" and user_guess == "Scissors") or
        (computer_choice == "Paper" and user_guess == "Rock") or
        (computer_choice == "Scissors" and user_guess == "Paper")
    ):
        return "Computer"
    else:
        return "User"
    
def main():
    # Variables to keep track of the score
    computer_wins = 0
    user_wins = 0

    while computer_wins < 3 and user_wins < 3:
        round_winner = play_round()

        if round_winner == "User":
            user_wins += 1
        elif round_winner == "Computer":
            computer_wins += 1

        # Print the current score
        print(f"\nScore - Computer: {computer_wins}, User: {user_wins}")

    # Print the overall winner
    if computer_wins == 3:
        print("Computer wins!")
    else:
        print("User wins!")

if __name__ == "__main__":
    main()
