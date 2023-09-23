def create_key_entry(key_entry="<b>Key</b>",entry_color=color.black,list_num=0):
    """
    Helps create a basic model key in Glowscript.org. The model key will be
    located in the top left hand corner of the "Run this program" preview canvas.
    :param key_entry: String name of the new entry to the key
    :param entry_color: Vector of the color in RGB format, vector(R,G,B)
    :param list_num: Integer placement of the key entry with 0 the title, 1 the second entry, etc.
    :return:
    """

    entry = label(pixel_pos=True, box=False, opacity=0, color=entry_color,
                  pos=vec(10,scene.height,0)-(list_num+1)*vec(0,20,0),
                  text=key_entry, align="left")
