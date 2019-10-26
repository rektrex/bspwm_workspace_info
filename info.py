#!/usr/bin/env python3

import os

colors = {
        'visible': '#88c563',
        'invisible': '#dfdfdf',
        'non-existent': '#e76d6d',
        }

visible_notification = "<span foreground='" + colors['visible'] + "'></span> "
invisible_notification = "<span foreground='" + colors['invisible'] + "'></span> "
non_existent_notification = "<span foreground='" + colors['non-existent'] + "'></span> "

bspwm_status = os.popen('bspc wm -g').read().split(':')[1:-3]
bspwm_status = list(map(lambda x: x[0], bspwm_status))

if 'O' in bspwm_status:
    last_visible = len(bspwm_status) - bspwm_status[::-1].index('O')

if 'o' in bspwm_status:
    last_invisibile = len(bspwm_status) - bspwm_status[::-1].index('o')

last_existent = max(last_visible, last_invisibile)

notification = ''

for i in range(last_existent):
    if bspwm_status[i] == 'O':
        notification += visible_notification
    elif bspwm_status[i] == 'o':
        notification += invisible_notification
    else:
        notification += non_existent_notification

os.system(f'notify-send -u Low " " "{notification}"')
