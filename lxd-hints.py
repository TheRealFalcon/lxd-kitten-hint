# Copy to ~/.config/kitty/lxd-hints.py
# Add to ~/.config/kitty/kitty.conf:
#   map kitty_mod+p>l kitten hints --customize-processing lxd-hints.py

import re


def mark(text, args, Mark, extra_cli_args, *a):
    # This function is responsible for finding all
    # matching text. extra_cli_args are any extra arguments
    # passed on the command line when invoking the kitten.
    # We mark all individual word for potential selection
    for idx, m in enumerate(re.finditer(r'^\|.*?\|', text, flags=re.MULTILINE)):
        start, end = m.span()
        mark_text = text[start+1:end-1].strip().replace('\n', '').replace('\0', '')
        # The empty dictionary below will be available as groupdicts
        # in handle_result() and can contain string keys and arbitrary JSON
        # serializable values.
        yield Mark(idx, start, end, mark_text, {})


def handle_result(args, data, target_window_id, boss, extra_cli_args, *a):
    boss.window_id_map.get(target_window_id).paste_text(data['match'][0])
