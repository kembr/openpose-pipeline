A project to automate calculation of joint angles frop openpose JSON output. 

Next steps:

  - Modify calc.py to operate on actual data (see /arms_output)
  - Modify calc.py to calculate the joint angle rather than summing x and y
  - Create a plot of joint angle changes (see /sample_plots)

NB: the json output in each file is printed to one line, which is unwieldy.
  If using vim you can use `:%!python -m json.tool` to pretty print the json
  in a more human readable form, or if using VSCode or similar try using an
  extension like "Prettify JSON".

