import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
pitch_image = Image.open("image.jpeg")

high_intensity_event_counts_complete = pd.read_csv('datasets/high_intensity_events.csv')

print("Producing Visualisation \nPlease be patient, this may take a good few minutes")

def get_zone_coordinates(zone): # Gets center of each zone for placing text
    if zone == 1:
        return (-35, 27.0575)
    elif zone == 2:
        return (-35, 0)
    elif zone == 3:
        return (-35, -27.0575)
    elif zone == 4:
        return (0, 27.0575)
    elif zone == 5:
        return (0, 0)
    elif zone == 6:
        return (0, -27.0575)
    elif zone == 7:
        return (35, 27.0575)
    elif zone == 8:
        return (35, 0)
    elif zone == 9:
        return (35, -27.0575)
    else:
        return (0, 0)

extent = [-52.5, 52.5, -34, 34]

list_of_participants = high_intensity_event_counts_complete['participation_id'].unique()

num_participants = len(list_of_participants)
fig, axes = plt.subplots(nrows=num_participants, ncols=1, figsize=(5, 3 * num_participants))

if num_participants == 1:
    axes = [axes]

for i, participant_id in enumerate(list_of_participants):
    participant_data = high_intensity_event_counts_complete[high_intensity_event_counts_complete['participation_id'] == participant_id]
    
    ax = axes[i]
    
    # Overlay pitch image
    ax.imshow(pitch_image, extent=extent, aspect='auto')

    # Plot high-intensity events grid
    for _, row in participant_data.iterrows():
        zone = row['Zone']
        x, y = get_zone_coordinates(zone)
        ax.text(x, y, str(row['High Intensity Event Count']), ha='center', va='center', fontsize=50, weight = 'bold')
    
    ax.axhline(y=-20.115, color='red', linestyle='-', linewidth=3, alpha=0.7)  # Adding a line at y = -34
    ax.axhline(y=20.115, color='red', linestyle='-', linewidth=3, alpha=0.7)  # Adding a line at y = 34
    ax.axvline(x=-17.5, color='red', linestyle='-', linewidth=3, alpha=0.7)  # Adding a line at y = -34
    ax.axvline(x=17.5, color='red', linestyle='-', linewidth=3, alpha=0.7)  # Adding a line at y = 34



    ax.set_title(f"Participant ID: {participant_id}")
    ax.set_xlim(extent[0], extent[1])
    ax.set_ylim(extent[2], extent[3])
    ax.axis('off')


plt.tight_layout()
plt.savefig("task_visualisation/high_intensity_event_areas.pdf")
plt.show()

print("Finished Producing visualisation")
