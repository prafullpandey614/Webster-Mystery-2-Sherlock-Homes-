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
