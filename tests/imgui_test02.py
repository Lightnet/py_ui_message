import pygame
from imgui.integrations.pygame import PygameRenderer
import OpenGL.GL as gl
import imgui
import sys

def main():
  pygame.init()
  size = 800, 600
  pygame.display.set_mode(size, pygame.DOUBLEBUF | pygame.OPENGL | pygame.RESIZABLE)

  imgui.create_context()
  impl = PygameRenderer()

  # initilize imgui context (see documentation)
  io = imgui.get_io()
  io.fonts.add_font_default()
  io.display_size = size

  is_running = True

  while is_running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit(0)
      impl.process_event(event)
    impl.process_inputs()
    # start new frame context
    imgui.new_frame()

    # open new window context
    imgui.begin("Your first window!", True)
    # draw text label inside of current window
    imgui.text("Hello world!")
    # close current window context
    imgui.end()


    # pass all drawing comands to the rendering pipeline
    # and close frame context
    gl.glClearColor(1, 1, 1, 1)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    #imgui.show_test_window()

    imgui.render()
    #imgui.end_frame()
    impl.render(imgui.get_draw_data())
    pygame.display.flip()

  print("Finish")

if __name__ == '__main__':
  main()