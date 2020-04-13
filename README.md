# AutoPi

This project can be used to expose your Raspberry Pi to the internet via SSH and automatically get an email notification of the Public address of Raspberry Pi. This is very useful when the Pi has been deployed in a remote location for some IoT project or is simply sitting at your home. All you need to do is power is up and you will get an email with an address to which you can SSH to.

Ngrok is used which relays the traffic from its public address to the Raspberry Pi. This can be used behind a NAT or even when your Raspberry Pi is connected to say a mobile hotspot.

The Ngrok service once started provides you with a public address which you can use to connect to the Raspberry Pi over the internet. Make sure to change your default login credentials before exposing Raspberry Pi to the internet.

After setting up Ngrok, two startup services are created. One for autostarting Ngrok, and another for emailing you the public Ngrok address.

# Installation

1. Register an account on Ngrok at https://dashboard.ngrok.com/signup

2. Download Ngrok to your home directory of Raspberry pi & Unzip:

    wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip
    
    unzip ngrok-stable-linux-arm.zip 
    
3. Connect Ngrok to your account. Go to your account and copy the authtoken from the dashboard and add it with:

    ./ngrok authtoken <your auth token>
  
4. Create a job to autostart ngrok on boot. For this copy the file ngrok.service to /lib/systemd/system/ngrok.service.
    
5. Enable the job to autostart with:

    systemctl enable ngrok.service
    
6. Modify the script notifier.py and place it in the home directory. Mailgun API has been used to send emails. You would need to create a mailgun account and get the API key and put it in script accordingly. The values that need to be replaced in the script are: [your api key here], [your mailgun domain name here],[your email address here]. Put them in without the [ ] brackets.

7. Create a job to autostart notifier service on boot. For this copy the file ngroknotifier.service to /lib/systemd/system/ngroknotifer.service.

8. Enable the job to autostart with:

    systemctl enable ngroknotifier.service
    
9. The next time Raspberry Pi is started, you would get an email with the ngrok public address. Connect over ssh to the ngrok address and the provided ngrok port.
