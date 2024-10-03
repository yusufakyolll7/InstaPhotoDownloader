import instaloader

L=instaloader.Instaloader()

def login_to_instagram(username, password):
    try:
        print("Logging in...")
        L.login(username, password)
        print(f"Logged in successfully as {username}")
    except instaloader.exceptions.BadCredentialsException:
        print("Error: Incorrect username or password.")
    except Exception as e:
        print(f"An error occured: {e}")

def download_photos(username):
    try:
        print(f"Downloading photos from {username}'s profile...")
        L.download_profile(username,profile_pic_only=False)
        print(f"Download completed for {username}.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Error: The profile '{username}' does not exist.")
    except Exception as e:
        print(f"An error occured: {e}")

if __name__ == "__main__":
    your_username=input("Enter your Instagram username: ")
    your_password=input("Enter your Instagram password: ")

    login_to_instagram(your_username,your_password)
    target_username=input("Enter the target Instagram username: ")
    download_photos(target_username)