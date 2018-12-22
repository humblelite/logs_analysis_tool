# Logs Analysis
Logs Analysis is a reporting tool that prints queries about the database **news**. The queries report:
* What are the most popular 3 articles of all times?
* Who are the most popular article authors of all times?
* On which days did 1% of request lead to errors?

App runs on python2 or python3. OS system in Virtual Box version 5.2,  _bento/ubantu-16.04_.

## Getting Started
#### Setting up Vagrant/Virtual Machine
 This reporting tool requires the installation of vagrant/virtual machine setup on your system. Follow the following
 steps for installation and setup. 
 
 * Use this link [Virtual Box](https://www.virtualbox.org/) to install latest virtual box which is version
  6.0 at this time.
 * Once Virtual Box is installed, use this link [Vagrant](https://www.vagrantup.com/) to install vagrant which
    is version 2.2.2 at this time.
 * After vagrant and virtual Box are installed on your system, go to this Github link
  [FSND](https://github.com/udacity/fullstack-nanodegree-vm) fork the repo and clone it.
 
 #### Running the virtual Machine.
 After FSND file is cloned ,``cd`` into folder. Then ``cd`` into the **vagrant** directory and follow these steps.
 
 * Run command ``vagrant up``
 * After vagrant is done installing  run command ``vagrant ssh``, to log into _bento/ubantu-16.04_ system.
 * Once you are logged in ``cd /vagrant``.
 
 #### Setting up database
 To setup log analysis database download data from this link 
 [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and follow these 
 steps.
 
* After newsdate.sql has downloaded unzip the file.
* place the file in the ``vagrant/`` directory of your FSND file. 
* go back into your vagrant/virtual machine OS from **running the virtual machine** steps above.
* ``ls`` inside the ``/vagrant``folder  to verify that the newsdata.sql file is in the folder.
* To load the data to the database run command ``psql -d news -f newsdata.sql``. This command will load the data to the
 **news** database that is already setup.
* run command ``\q`` to exit psql.

#### Running log analysis tool
Place the logs_analysis folder in the ``vagrant/`` directory of your **FSND** folder and follow commands below to run tool.
```bash
$cd logs_analysis
$python logs.py

```

