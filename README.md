A project to automate calculation of joint angles frop openpose JSON output. 

Next steps:

  - Create a plot of joint angle changes (see /sample_plots) using Matplotlib.

NB: the json output in each file is printed to one line, which is unwieldy.
  If using vim you can use `:%!python -m json.tool` to pretty print the json
  in a more human readable form, or if using VSCode or similar try using an
  extension like "Prettify JSON".

