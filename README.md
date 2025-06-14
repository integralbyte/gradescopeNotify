# GradescopeNotify

**GradescopeNotify** is a Python script that periodically checks for assignment results on Gradescope and sends a notification to a Discord webhook when grades are released. You can run this in the background on the day your assignment marks are supposed to be released to receive a notification as soon as they're available!

## Setup

When you run the script, you will be prompted to enter the following four inputs:

1. **Assignment Number**
   The script uses this number to identify which assignment’s grades to monitor.

   * The first (oldest) assignment is numbered **1**.
   * If you have 4 assignments total, the newest one is numbered **4**.

2. **Assignment Name**
   A custom name to be displayed in the Discord notification.

   * This does **not** need to match the name on Gradescope.
   * It’s only used for the notification message.

3. **Gradescope `signed_token` Cookie**
   Your Gradescope authentication token.

   * You can find this in your browser’s developer tools under the “Cookies” section while logged into Gradescope.

4. **Course ID**
   The 6-digit ID of the course where the assignment is hosted.

   * This can be found in the course URL:
     `https://www.gradescope.com/courses/XXXXXX`
