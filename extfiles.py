import os
import datetime
import pathlib

for dr, dn, fn in os.walk(r'D:\test'):
    c_time = os.path.getctime(dr)

    dt_c = datetime.datetime.fromtimestamp(c_time)

    print()

    print('current path :', dr)

    if dn:
        print("No of directories -", len(dn))
        for i in range(len(dn)):
            drpath = os.path.join(dr, dn[i])
            c_time = os.path.getctime(drpath)

            dt_c = datetime.datetime.fromtimestamp(c_time).replace(microsecond=0)

            print('directory Name :', dn[i], "\tCREATED ON - ", dt_c, "\tPath - ", drpath)

    else:
        print("No directries found in this path ")

    if fn:
        print("No of files -", len(fn))
        for i in range(len(fn)):
            # print(len(fn))
            filepath = os.path.join(dr, fn[i])
            f_name = pathlib.Path(filepath)
            c_timestamp = f_name.stat().st_ctime
            c_timefile = datetime.datetime.fromtimestamp(c_timestamp).replace(microsecond=0)

            print('file Name :', fn[i], "\tCREATED ON - ", c_timefile, "\tPath - ", filepath)

    else:
        print("No file Exists in the current path")

    print()
    print('-' * 150)
    print()

# test = {"testone": {"ep401": {"sq001": ["sh001", "sh002"]}}, "test": {"ep401": {"sq001": ["sh001", "sh002"]}}}
# test = {"sh":{"ma":[], "png":[]}}
#
# aa = {"proj":{"ep":{'sq':{"sh":{"latest_version":[], "missing_version":[], "lower_ver":[]}}}}}
# {'dnn': {'ep402': {'sq002': ['sh0290']}}
# import re
# datata=[r'R:/05_edit/From_Edit/Animatics/EP402/Audios/rh4_ep402_sh0290.wav', 'R:/asset_lib/assets/ep_400/animals/rig/rh4_400_ani_rooster.ma\\" 656957808 \\"R:/asset_lib/assets/ep_400/animals/rig/rh4_400_ani_rooster.ma\\" \\"FileRef\\"\\n1\\n\\"rh1_00_cha_littlejohnRN\\" \\"\\" \\"R:/asset_lib/assets/mainpack/chars/rig/rh1_00_cha_littlejohn.ma\\" 3828727255 \\"R:/asset_lib/assets/mainpack/chars/rig/rh1_00_cha_littlejohn.ma\\" \\"FileRef\\"\\n2\\n\\"rh1_00_cha_tuckRN\\" \\"\\" \\"R:/asset_lib/assets/mainpack/chars/rig/rh1_00_cha_tuck.ma\\" 1197556469 \\"R:/asset_lib/assets/mainpack/chars/rig/rh1_00_cha_tuck.ma\\" \\"FileRef\\"\\n3\\n\\"shot_camRN\\" \\"\\" \\"R:/07_tools/camera/shot_cam.ma\\" 2474136977 \\"R:/07_tools/camera/shot_cam.ma\\" \\"FileRef\\"\\n4\\n\\"rh3_00_set_castle_env_hiRN\\" \\"\\" \\"R:/asset_lib/assets/mainpack/sets/rig/rh3_00_set_castle_env/rh3_00_set_castle_env_hi.ma\\" 3848238319 \\"R:/asset_lib/assets/mainpack/sets/rig/rh3_00_set_castle_env/rh3_00_set_castle_env_hi.ma\\" \\"FileRef\\"\\n5\\n\\"rh1_00_cha_castleguard_a4RN\\" \\"\\" \\"R:/asset_lib/assets/mainpack/chars/rig/rh1_00_cha_castleguard_a4.ma\\" 245200536 \\"R:/asset_lib/assets/mainpack/chars/rig/rh1_00_cha_castleguard_a4.ma\\" \\"FileRef\\"\\n6\\n\\"rh1_00_pro_littlejohn_bludgeonRN\\" \\"\\" \\"R:/asset_lib/assets/mainpack/props/rig/rh1_00_pro_littlejohn_bludgeon.ma\\" 508018636 \\"R:/asset_lib/assets/mainpack/props/rig/rh1_00_pro_littlejohn_bludgeon.ma\\" \\"FileRef\\"\\n7\\n\\"rh1_00_ani_derkesthai_quadRN\\" \\"\\" \\"R:/asset_lib/assets/mainpack/animals/rig/rh1_00_ani_derkesthai_quad.ma\\" 1567618038 \\"R:/asset_lib/assets/mainpack/animals/rig/rh1_00_ani_derkesthai_quad.ma\\" \\"FileRef\\"\\n8\\n\\"rh1_00_pro_littlejohn_bludgeonRN1\\" \\"\\" \\"R:/asset_lib/assets/mainpack/props/rig/rh1_00_pro_littlejohn_bludgeon.ma\\" 508018636 \\"R:/asset_lib/assets/mainpack/props/rig/rh1_00_pro_littlejohn_bludgeon.ma\\" \\"FileRef\\"\\n9\\n\\"RH4_ep402_sh0290_audio\\" \\"filename\\" \\"R:/05_edit/From_Edit/Animatics/EP402/Audios/rh4_ep402_sh0290.wav', 'R:/05_edit/From_Edit/Animatics/EP402/Audios/rh4_ep402_sh0290.wav']
# d=re.findall(r'\b\w+\.ma\b',datata)
# print(d)