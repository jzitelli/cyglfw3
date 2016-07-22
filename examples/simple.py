from OpenGL import GL as gl
import glfw3 as glfw

if not glfw.Init():
    exit(1)

window = glfw.CreateWindow(640, 480, "Simple Example")
if not window:
    glfw.Terminate()
    exit(1)

def key_callback(window, key, scancode, action, mods):
    if (key == glfw.GLFW_KEY_ESCAPE and action == glfw.GLFW_PRESS):
        glfw.SetWindowShouldClose(window, gl.GL_TRUE)

glfw.SetKeyCallback(window, key_callback)

glfw.MakeContextCurrent(window)
while not glfw.WindowShouldClose(window):
    width = 680
    height = 480
    # frame_size = glfwGetFrameBufferSize(window, width, height)
    ratio = width / float(height)

    gl.glViewport(0, 0, width, height)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    gl.glOrtho(-ratio, ratio, -1.0, 1.0, 1.0, -1.0)
    gl.glMatrixMode(gl.GL_MODELVIEW)

    gl.glLoadIdentity()
    gl.glRotatef(float(glfw.GetTime() * 50), 0, 0, 1)

    gl.glBegin(gl.GL_TRIANGLES)
    gl.glColor3f(1.0, 0.0, 0.0)
    gl.glVertex3f(-0.6, -0.4, 0.0)
    gl.glColor3f(0.0, 1.0, 0.0)
    gl.glVertex3f(0.6, -0.4, 0.0)
    gl.glColor3f(0.0, 0.0, 1.0)
    gl.glVertex3f(0.0, 0.6, 0.0)
    gl.glEnd()

    glfw.SwapBuffers(window)
    glfw.PollEvents()

glfw.DestroyWindow(window)
glfw.Terminate()
exit()
