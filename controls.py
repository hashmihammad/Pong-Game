def setup_controls(screen, r_paddle, l_paddle):
    keys = {
        "Up": {"pressed": False, "action": r_paddle.go_up},
        "Down": {"pressed": False, "action": r_paddle.go_down},
        "w": {"pressed": False, "action": l_paddle.go_up},
        "s": {"pressed": False, "action": l_paddle.go_down}
    }

    def press(key):
        keys[key]["pressed"] = True
        move_continuously(key)

    def release(key):
        keys[key]["pressed"] = False

    def move_continuously(key):
        if keys[key]["pressed"]:
            keys[key]["action"]()
            screen.ontimer(lambda: move_continuously(key), 50)

    for key in keys:
        screen.onkeypress(lambda k=key: press(k), key)
        screen.onkeyrelease(lambda k=key: release(k), key)

    screen.listen()
