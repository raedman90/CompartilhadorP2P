import os

def list_public_files():
    public_dir = "./public"
    if not os.path.exists(public_dir):
        os.makedirs(public_dir)
    return [(file, os.path.getsize(os.path.join(public_dir, file))) for file in os.listdir(public_dir) if os.path.isfile(os.path.join(public_dir, file))]