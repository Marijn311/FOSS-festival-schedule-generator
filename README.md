# Festival Show Scheduler

This Python script helps you schedule multiple shows at a festival across a minimum number of stages. It ensures that no two overlapping shows are scheduled on the same stage.

## Features

- **Automatic Scheduling**: Automatically assigns shows to stages, minimizing the number of stages required.
- **Conflict-Free**: Ensures that no two shows that overlap in time are placed on the same stage.
- **Visual Output**: Generates a nicely formatted table where stages are on the x-axis, and hours are on the y-axis, displaying which show is playing on which stage at any given time.

## How It Works

The script first sorts the shows by their start and end times. It then assigns each show to an available stage, creating new stages as necessary to accommodate all shows. Finally, it outputs a table showing the schedule.
### Example

Given the following shows in a CSV file:

```csv
show_name,start_time,end_time
show_1,36,39
show_2,30,33
show_3,29,36
show_4,40,45
show_5,32,38
```

The output table will look as follows:

| Hour | Stage 1 | Stage 2 | Stage 3 |
|------|---------|---------|---------|
| 29   | show_3  |         |         |
| 30   | show_3  | show_2  |         |
| 31   | show_3  | show_2  |         |
| 32   | show_3  | show_2  | show_5  |
| 33   | show_3  | show_2  | show_5  |
| 34   | show_3  |         | show_5  |
| 35   | show_3  |         | show_5  |
| 36   | show_3  | show_1  | show_5  |
| 37   |         | show_1  | show_5  |
| 38   |         | show_1  | show_5  |
| 39   |         | show_1  |         |
| 40   | show_4  |         |         |
| 41   | show_4  |         |         |
| 42   | show_4  |         |         |
| 43   | show_4  |         |         |
| 44   | show_4  |         |         |
| 45   | show_4  |         |         |


The output table will look as follows:

| Hour | Stage 1 | Stage 2 | Stage 3 |
|------|---------|---------|---------|
| 29   | show_3  |         |         |
| 30   | show_3  | show_2  |         |
| 31   | show_3  | show_2  |         |
| 32   | show_3  | show_2  | show_5  |
| 33   | show_3  | show_2  | show_5  |
| 34   | show_3  |         | show_5  |
| 35   | show_3  |         | show_5  |
| 36   | show_3  | show_1  | show_5  |
| 37   |         | show_1  | show_5  |
| 38   |         | show_1  | show_5  |
| 39   |         | show_1  |         |
| 40   | show_4  |         |         |
| 41   | show_4  |         |         |
| 42   | show_4  |         |         |
| 43   | show_4  |         |         |
| 44   | show_4  |         |         |
| 45   | show_4  |         |         |
