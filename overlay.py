def func(img_path):
	horizontal_frame_number = 605  #in pixels
	vertical_frame_number = 80 
	new_width = 530
	new_height = 880
	cmd = [
		'ffmpeg',
		'-i', 'background.png',                # Background image
		'-i', f'{img_path}',                    	   # Input image
		'-i', f'{img_path}',                    	   # Duplicate of the input image
		'-filter_complex',
		f'[1:v]scale={new_width}:{new_height}[resized]; [0:v][resized]overlay=x={horizontal_frame_number}:y={vertical_frame_number}',  # Resize and overlay
		'-c:a', 'copy',
		'output.png'
	]

	try:
		subprocess.run(cmd, check=True)
		return Response({"message": "Image overlay successful"}, status=status.HTTP_200_OK)
	except subprocess.CalledProcessError as e:
		return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
from urllib import response
from django.shortcuts import get_object_or_404

import subprocess 

from rest_framework import status,generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import ProfileSerializer
from ..models import UserProfile,ChallengeParticipant
from ..permissions import IsNotSuspended
from ..mails import send_invitation,send_mail_when_new_tig_arrives

# pylint: disable=maybe-no-member

class InviteMail(generics.CreateAPIView):
	permission_classes = [IsAuthenticated,IsNotSuspended]

	def post(self,request,*args,**kwargs):
		return send_invitation(request.data['emailAddress'],request.user)

class ColdRecommendationSystem(generics.ListAPIView):
	permission_classes = [IsAuthenticated,IsNotSuspended]
	serializer_class = ProfileSerializer

	def get(self,request,*args,**kwargs):
		#top 10 users with most challenges performed
		# most_active_users = ChallengeParticipant.objects.order_by().values('challenger__username').annotate(num_challenges=Count('challenge')).order_by('-num_challenges')[:10]

		# users = UserProfile.objects.filter(Q(username__in=most_active_users.values('challenger__username')))
		users = UserProfile.objects.exclude(user_image__icontains='avatar')[:10]
		serializer = self.serializer_class(users,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)

class AndroidPushNotificationChannelList(generics.RetrieveAPIView):
	permission_classes = []
	
	def get(self, request, *args, **kwargs):
		channel_list = [{
			'id': 'like-channel',
			'name': 'Like Channel',
			},{
			'id': 'comment-channel',
			'name': 'Comment Channel',
			},{
			'id': 'public-channel',
			'name': 'Public Channel',
		}]
		return Response(channel_list,status=status.HTTP_200_OK)
def func(img_path):
	horizontal_frame_number = 605  #in pixels
	vertical_frame_number = 80 
	# new_width = 530
	# new_height = 880
	new_width = 530              # Replace with the desired width in pixels for the resized image
	new_height = 880             # Replace with the desired height in pixels for the resized image
	horizontal_frame_number = 0  # Replace with the horizontal frame number for overlay
	vertical_frame_number = 0    # Replace with the vertical frame number for overlay

	back_width =    0# Replace with the actual width of the back image
	back_height = 880  # Replace with the actual height of the back image
	resized_back_width = 530   # Replace with the desired width for the resized back image
	resized_back_height = 880  # Replace with the desired height for the resized back image

	# cmd = [
	# 	'ffmpeg',
	# 	'-i', img_path,           # Background image
	# 	'-i', '.png',          # Front image
	# 	 '-filter_complex',
	# 	f'[0:v]scale={resized_back_width}:{resized_back_height}[resized_back]; [resized_back][1:v]overlay=0:0:enable=\'lt(mod(N,1),0.1)\'',  # Resize and overlay
	# 	'-c:a', 'copy',
	# 	'output2.png'
	# ]
	# cmd = [
	# 	'ffmpeg',
	# 	'-i', img_path,           # Background image
	# 	'-i', 'background.png',          # Front image
	# 	'-filter_complex',
	# 	'-filter_complex',
	# 	f'[0:v]scale={resized_back_width}:{resized_back_height}[resized_back]; f'[0:v]scale={resized_back_width}:{resized_back_height}[resized_back]; [resized_back][1:v]overlay=0:0:enable= "lt(mod(N,1),0.1)"  ',  # Resize and overlay
	# 	'-c:a', 'copy',
	# 	'output.png'
	# ]
	ffmpeg_command = [
    'ffmpeg',
    '-i', 'man.png',
    '-i', 'bb.png',
    '-i', 'play.png',
    '-filter_complex',
    "[1:v]format=yuva420p,geq=lum='p(X,Y)':a='if(gt(abs(W/2-X),W/2-50)*gt(abs(H/2-Y),H/2-50),if(lte(hypot(50-(W/2-abs(W/2-X)),50-(H/2-abs(H/2-Y))),50),255,0),255)'[rounded];"
    "[rounded]scale=175:312[small_resized];"
    "[small_resized][2:v]overlay=(W-w)/2:(H-h)/2[poster];"
    "[0:v][poster]overlay=182:3:format=auto",
    'out.png'
	]
	cmd1 = [
    "ffmpeg",
    "-i", img_path,
    "-vf", "scale=530:880",
    "output_resized.png"
	]
	# ffmpeg_command = [
	# 	'ffmpeg',
	# 	"-i", "output_resized.png",        # Replace with the actual path to image A
	# 	"-i", "background.png",   
	# 	'-filter_complex',  '[1:v]scale=w=iw:h=ih[bg];[0:v][bg]overlay=x=0:y=0:shortest=1',
	# 	"output_file.png"
	# ]
	cmd = [
    "ffmpeg",
    "-i", "output_resized.png",        # Replace with the actual path to image A
    "-i", "background.png",        # Replace with the actual path to image B
    "-filter_complex", "[0:v]scale=w=iw*min(iw*1.0/iw,iw*1.0/ih):h=ih*min(iw*1.0/iw,iw*1.0/ih)[scaled];[1:v][scaled]overlay=x=0:y=0",
    "output_overlay.png"
	]


	# cmd = [
    # "ffmpeg",
    # "-i", "output_resized.png",
    # "-i", "background.png",
    # "-filter_complex", "[1:v][0:v]overlay=x=490:y=80:shortest=1",
    # "output_overlay.png"
	# ]





	try:
		# subprocess.run(cmd1, check=True)
		subprocess.run(ffmpeg_command, check=True)
		return Response({"message": "Image overlay successful"}, status=status.HTTP_200_OK)
	except subprocess.CalledProcessError as e:
		return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AddVideoPosterToBackgroundImage(APIView):
	def get(self, request):
		im_path = "feynman.png"
		func(img_path=im_path)
		return Response({'Status' : 'done'},status=status.HTTP_200_OK)
