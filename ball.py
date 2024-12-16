import cairo

# Image dimensions
WIDTH, HEIGHT = 400, 400

# Create a surface and a context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Draw background
context.set_source_rgb(1, 1, 1)  # White background
context.rectangle(0, 0, WIDTH, HEIGHT)
context.fill()

# Draw the red sphere
cx, cy = WIDTH // 2, HEIGHT // 2  # Center of the sphere
radius = 50  # Sphere radius

# Create a radial gradient to simulate 3D shading
gradient = cairo.RadialGradient(cx - 20, cy - 20, 10, cx, cy, radius)
gradient.add_color_stop_rgb(0, 1, 0, 0)  # Bright red at the center
gradient.add_color_stop_rgb(1, 0.5, 0, 0)  # Darker red at the edges

# Set the gradient as the source
context.set_source(gradient)
context.arc(cx, cy, radius, 0, 2 * 3.14159)  # Draw the sphere as a circle
context.fill()

# Save the image
surface.write_to_png("red_sphere.png")
print("Red sphere drawn and saved as 'red_sphere.png'")
