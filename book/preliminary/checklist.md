# Checklist
## Required setup

```{attention}
Please make sure to find some time to go through the below material before
the hackweek.

__Upon completion of this pre-event work you will have__:
<div>
  <input type="checkbox" name="a2">
  <label for="a2">Created an EarthData Login</label>
</div>
<div>
  <input type="checkbox" name="a3">
  <label for="a3">Created a GitHub account</label>
</div>
<div>
  <input type="checkbox" name="a4">
  <label for="a4">Can login to the CryoCloud JupyterHub</label>
</div>
<div>
  <input type="checkbox" name="a5">
  <label for="a5">Review material from 2022 PACE course (Optional)</label>
</div>
```

### EarthData Login

Each participant will need a login to access NASA data from within the Python Jupyter Notebooks. 
You will need to enter your Earthdata username and password in order for this to work. If you do 
not already have an Earthdata login, then navigate to the Earthdata login [page](https://urs.earthdata.nasa.gov/), 
register, and record username and password somewhere for use during the hackweek. 

### GitHub Account

[GitHub](https://github.com/) is a hosting service for [Git](https://icesat-2-2023.hackweek.io/reference/glossary.html#term-Git)
repositories, enabling us to share code across teams in a web environment.
There are three reasons you are required to have a GitHub account for the hackweek:
Your GitHub account will give you access to the hackweek cloud computing resources
Project teams will be encouraged to use GitHub to collaborate and work together on their code
If you do not already have a GitHub account, then navigate to [GitHub](https://github.com/)
and enter your email address and click on the green ‘Sign up for GitHub’ button. 
You will need to answer a few required questions in the following dialogs. Be sure to save your username 
and password somewhere for use during the hackweek.

(accessing-jupyterhub)=
### CryoCloud JupyterHub

We will be using a shared cloud environment called a [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/) for the hackweek. 
All that is required is a web browser and a GitHub username for authentication. 
We are partnering with [CryoCloud](https://book.cryointhecloud.com/intro.html), which is a JupyterHub built for NASA Cryosphere and Earth Science communities.
Please follow these instructions which will guide you through gaining access to the CryoCloud. 

1. Fill out this short [Getting Started Survey](https://forms.gle/d8oP1gp9YikS2ixM8) to provide the required credentials and information to get you on the hub. 


2. Within the next day or two, you will receive an invite to the CryoCloud Github organization and CyroCloudUsers team. This will be an email from GitHub at the email you have linked to your GitHub profile. Please accept this invitation within 7 days or it will disappear and we will have to resend it. Your membership on that GitHub team provides you with access to the CryoCloud. You will be invited to the CryoCloud Slack at the same time.


3. Open up the CryoCloud JupyterHub to make sure it works for you:  https://hub.cryointhecloud.com/. You will need your GitHub username and password to sign on. 


It can take several minutes for new servers to launch on the cloud. Once things are spun up, you will see your very own instance of a JupyterLab environment. 

You will have access to your own virtual drive space under the `/home/jovyan` directory. No other users will be able to see or access your data files. You can add/remove/edit files in your virtual drive space. You will also have access to the `shared` folder (read-only access), and to the *`shared-public`* folder (read and write access). These are shared spaces so please make sure not to delete files from here unless they are yours.

*To save our community money, when you are finished working for the day it is really helpful for you to explicitly stop your server before logging out of your JupyterHub session.* To shut your server down immediately when you’re exiting your session please select “File -> Hub Control Panel -> Stop my Server” then you can click the “Log Out” button. We ask this because when you keep a session active it uses up AWS resources and these resources cost money per hour of use. If you forget this step, though, the server will shut down automatically after 90 min of no use.
Logging out will **NOT** cause any files under `/home/jovyan` to be deleted. It is equivalent to turning off your desktop computer at the end of the day.

4. Add yourself to the CryoCloud #pace_hackweek [Slack channel](https://join.slack.com/t/cryospherecloud/shared_invite/zt-1isgbeuhh-q~cYYKtn_6i3PR1alGca_g) to join the community, get updates, and ask any questions. 
