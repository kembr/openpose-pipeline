A project to automate calculation of joint angles frop openpose JSON output. 

Next steps:

  - √ ~~Make sure generated plots of joint angle changes are saved to an output folder.~~
  - Combine overlapping code into fewer files. (Main execution file, with functions helper file)
  - Goal: have a workable demo which will:
      1. trigger openpose
      2. capture json output
      3. calculate the appropriate joint angles and save results.
      4. generate save the graphs.

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

