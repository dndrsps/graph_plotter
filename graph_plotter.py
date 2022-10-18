import window as wd
import screen as scr

gui_window = wd.Window()
graph_screen = scr.GraphScreen(1000, 1000, (255, 255, 255))

def main():

    running = True
    while running:
    
        gui_window.refresh()
        running = graph_screen.refresh(gui_window.get_data(), gui_window.slider.get())

    exit()

if __name__ == "__main__":

    main()


