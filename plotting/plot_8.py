# Import matplotlib.pyplot
import matplotlib.pyplot as plt

from plotting.plot_co import physical_sciences, computer_science, year, health, education
# Plot with legend as before
plt.plot(year, computer_science, color='red', label='Computer Science')
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='bottom right')

# Compute the maximum enrollment of women in Computer Science: cs_max
cs_max =computer_science.max()

# Calculate the year in which there was maximum enrollment of women in Computer Science: yr_max
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum', xy = (yr_max, cs_max), xytext = (yr_max+5, cs_max+5),  arrowprops=dict(facecolor='k') )

# Add axis labels and title
plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()
