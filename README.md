A project to automate calculation of joint angles frop openpose JSON output. 

Heplful flags:  
  `--write_json <path>`: specify path to save json output files.  
  `--write_video <path>`: specifiy path to save rendered video output.  
  `--write_video_with_audio false`: if input is a video, rendered video output will not be saved with audio  
  `--disable_blending true`: renders keypoint skeletons on black background instead of original video  

Command to run quickly on one person:  
`bin\OpenPoseDemo.exe --video [video_file] --write_json [output_folder] --tracking 1 --number_people_max 1`

NB: the json output in each file is printed to one line, which is unwieldy.
  If using vim you can use `:%!python -m json.tool` to pretty print the json
  in a more human readable form, or if using VSCode or similar try using an
  extension like "Prettify JSON".