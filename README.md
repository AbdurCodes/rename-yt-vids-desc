Bulk youtube video description text edit with python script 

Using this python script i was able to replace some of the text in my youtube videos descriptions with some other text (that was amazing)

-First create a new folder
-Inside that folder, create a virtual environment (python<version> -m venv <virtual-environment-name>)
-env/Scripts/activate to activate the virtual environment
-install the dependencies > pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
-now you can run the python script > python script_name
-if all is well, it will take you to your specific youtube channel that you want to deal with, authorize it, once authenticated you can close the window and come to your vscode terminal, the magic can be seen there happening
-after the script finishes executing, you can check the youtube vids desc and confirm whether the changes took place
-at the end you can come out of the virtual environment by command 'deactivate'





>>>>>>>>>> STEPS to enable the YouTube Data API v3 <<<<<<<<<<<
Step 1: Access Google Cloud Console
Go to https://console.cloud.google.com/

Step 2: Create a New Project 
- Click on the project dropdown at the top.  
- Select "New Project".  
- Enter a project name and click "Create".

Step 3: Enable YouTube Data API v3
- In the left sidebar, click "APIs & Services" > "Library"  
- Search for "YouTube Data API v3" 
- Click on it and press "Enable"

Step 4: Create OAuth 2.0 Credentials 
- Go to "APIs & Services" > "Credentials" 
- Click "Create Credentials" > "OAuth client ID"  
- Configure the OAuth consent screen (choose "External" for personal use) 
- For application type, select "Desktop App"  
- Download the `client_secrets.json` file

Step 5: Add `client_secrets.json` to Your Project
Place the downloaded `client_secrets.json` file in the same folder as your Python script





To download the `client_secrets.json` file, follow these steps after setting up the OAuth consent screen:

### **Step 1: Create OAuth 2.0 Credentials**  
1. In the **Google Cloud Console**, go to **APIs & Services > Credentials**.  
2. Click on **"Create Credentials"** and select **"OAuth client ID"**.  

### **Step 2: Configure OAuth Client**  
1. **Application Type** → Select **"Desktop App"**.  
2. **Name** → Enter any name (e.g., `"YouTube Bulk Updater"`).  
3. Click **"Create"**.

### **Step 3: Download Client Secret**  
1. After creation, you will see the newly created OAuth 2.0 client.  
2. Click the **Download** button (a downward arrow icon) next to your new credential.  
3. This will download the **`client_secrets.json`** file.

### **Step 4: Place the File in Your Project Folder**  
Move the downloaded **`client_secrets.json`** file into the same folder as your Python script.





If you get this error
FileNotFoundError: [Errno 2] No such file or directory: 'client_secrets.json' 
This error means the script cannot find the `client_secrets.json` file in the directory where it’s being executed

### **How to Fix It**

1. **Locate the Downloaded File:**  
   - Check your **Downloads** folder for `client_secrets.json`.  
   - Sometimes it may have a different name like `client_secret_<client-id>.json`.  

2. **Rename the File (if needed):**  
   - If the file has a different name, rename it to **`client_secrets.json`**.  

3. **Move the File to the Correct Folder:**   
   - This must be the same folder where your script is located

4. **Run the Script Again:**  
   python renameYTvidsDesc.py





**Error 403: access_denied**
Causes of Error 403: access_denied: usually happens due to one of the following reasons
-YouTube Data API is Not Enabled
-OAuth Consent Screen Not Published
-Incorrect OAuth Scopes
-Using a Restricted or Incorrect Google Account

### **Fixes**

#### **1. Enable YouTube Data API v3 (Double-check)**  
- Go to [Google Cloud Console](https://console.cloud.google.com/).  
- Navigate to **APIs & Services > Library**.  
- Search for **"YouTube Data API v3"**.  
- Click **Enable** if it’s not already enabled.

#### **2. Publish the OAuth Consent Screen**  
- Go to **APIs & Services > OAuth consent screen**.  
- If the status shows **"Testing"**, click **Publish App**.  
- This allows the app to request access without restrictions.

#### **3. Verify OAuth Scopes**  
- The script uses this scope:  
  ```
  https://www.googleapis.com/auth/youtube.force-ssl
  ```  
- Make sure this scope is **added** and **approved** on the OAuth consent screen.  
  - Go to **OAuth consent screen** → **Edit App** → **Scopes**.  
  - Add the above scope if it's missing.

#### **4. Use the Correct Google Account**  
- Log in with the **same Google account** linked to your YouTube channel.  
- If you have multiple accounts, try using an incognito window to avoid account mix-ups.

#### **5. Delete `token.pickle` and Retry**  
- Sometimes, old authentication tokens cause issues.  
- Delete the `token.pickle` file in your project folder.  
- Run the script again to trigger a fresh authentication.








### **To Confirm The Script Worked 🎉 :**

1. **Check Your YouTube Videos:**  
   - Go to **YouTube Studio** → **Content**.  
   - Open a few video descriptions and check if the old text was replaced with the new text.

2. **Verify the Output:**  
   - Did the script print messages like:  
     ```
     Updated video ID <video_id>
     ```
   - This confirms that video descriptions were updated.



### **If Everything Looks Good, You're Done! ✅**
