import os,sys
import subprocess
# to check whether a user exists
def if_user_exists(username):
	cmd= "id -u %s" %username
	try:
		output= subprocess.getoutput(cmd)
		#x=type(output)
		#print(x)
		if ":" not in output:
			return("True") #user doesn't exist
		else:
			return("False") 
		'''
		if output.split(':')[2] != " no such user":
			#print(output.split(':')[2])
			
			return("True") # User exist
		else:
			return("False")'''
	except Exception:
		return (Exception)

#Create User
#useradd -p $(openssl passwd -1 abcd@ert) suranjan
#cmd='useradd -d %s -p $(openssl passwd -1 %s) -a -G sudo %s ' %(HOME_DIRECTORY, password,username)
#useradd -d /home/suranjan1 -p $(openssl passwd -1 abcd@ert) --shell /bin/bash suranjan


class createUser:

	def __init__(self):
		pass

	def createUser_1(self,username,home_directory,sudo_access,login_shell,password):
	#check if a user exists
		check_user=if_user_exists(username)
		if check_user=="True":
			return("User Already Exists!! Can't Create User with same Username. However you can try modifying the user")

		# Add user with home directory, password,login shell,
		#print(username,home_directory,sudo_access,login_shell,password)
		cmd='sudo useradd -d %s -p $(openssl passwd -1 %s) --shell %s %s' %(home_directory,password,login_shell,username)

		try:

			output= subprocess.getoutput(cmd)

		except Exception:
			return(Exception)
		#give sudo access to user
		if(sudo_access=="Yes"):
			cmd_sudo='sudo usermod -a -G sudo %s' %username
			sudo_output= subprocess.getoutput(cmd_sudo)
			return("User %s created with sudo access" %username)

		return("User %s created without sudo access" %username)

	#change default login
	#cmd_default_login='usermod --shell %s %s' %(login_shell,username)
	#default_login= subprocess.getoutput(cmd_default_login)

	#modify User
	#usermod -d home_directory -p $(openssl passwd -1 abcd@ert) --shell /bin/bash suranjan
	#remove sudo user 'gpasswd -d student research'
	def modifyUser(self,username,home_directory,sudo_access,login_shell,password):
		#check if a user exists
		check_user=if_user_exists(username)
		if check_user=="False":
			return("User doesn't exist!! First create user")
			

		# useradd -d homedirectoy username
		cmd='usermod -d %s -p $(openssl passwd -1 %s) --shell %s %s' %(home_directory,password,login_shell,username)
		try:
			output= subprocess.getoutput(cmd)
		except Exception:
			return (Exception)
		#give sudo access to user
		if sudo_access=="No":
			cmd_sudo='gpasswd -d %s sudo' %username
			try:
				sudo_output= subprocess.getoutput(cmd_sudo)
			except Exception:
				return (Exception)
			return("User %s modified without sudo access" %username)

		if(sudo_access=="Yes"):
			cmd_sudo='sudo usermod -a -G sudo %s' %username
			try:
				sudo_output= subprocess.getoutput(cmd_sudo)
			except Exception:
				return (Exception)
			
			return("User %s modified with sudo access" %username)
		#change default login
		#cmd_default_login='usermod --shell %s %s' %(login_shell,username)
		#default_login= subprocess.getoutput(cmd_default_login)


	#delete user userdel --remove username

	def deleteUser(self,username):
		check_user=if_user_exists(username)
		if check_user=="True":
			cmd='userdel --remove %s' %username 
			try:

				output=subprocess.getoutput(cmd)

			except Exception:
				return (Exception)
			return ("User %s deleted" %username)
		else:
			return("User doesn't exist!!")
	def parse_logic(self,input_request):
		username= input_request['username']
		home_directory= input_request['home_folder']
		sudo_access=input_request['sudo']
		login_shell=input_request['shell_type']
		password=input_request['user_password']
		operation=input_request['operation']
		if input_request['operation']=='create':
			result=self.createUser_1(username,home_directory,sudo_access,login_shell,password)
			
		if input_request['operation']=='modify':
			result=self.modifyUser(username,home_directory,sudo_access,login_shell,password)
			
		if input_request['operation']=='delete':
			result=self.deleteUser(username)
		return (result)	
		

		#print(username,home_directory,sudo_access,login_shell,password,operation)

#def main():
#	createUser(sys.argv[1])

#if __name__ == "__main__":
#	main()

