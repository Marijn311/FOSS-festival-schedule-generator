import pandas as pd

if __name__ == "__main__":
    def schedule_shows(shows):
        """
        Schedule the shows to the minimum number of stages required.

        Parameters:
        shows (list of tuples): A list where each tuple contains the show name, start, and end time.

        Returns:
        list of tuples: A list of tuples with show name, start time, end time, and assigned stage.
        int: The minimum number of stages required.
        """

        # Sort shows by start time (and by end time as a tie-breaker)
        shows.sort(key=lambda x: (x[1], x[2]))

        # Track the stage assignment and available stages
        stage_assignments = [] # List of tuples for all the scheduled shows (show_name, start_time, end_time, assigned_stage)
        stages_end_times = []  # List to track the end times of currently occupied stages
        stage_count = 0        # Number of stages minimally needed to make the schedule

        # Loop over all shows and assign them to a stage
        for show in shows:
            show_name, start_time, end_time = show

            # Find a stage that is free (where the last show ends before the current show starts)
            assigned_stage = None
            for i in range(len(stages_end_times)):
                if stages_end_times[i] < start_time:
                    assigned_stage = i + 1
                    stages_end_times[i] = end_time
                    break

            # If the search for a free existing stage fails, increase the number of stages.
            if assigned_stage is None:
                stage_count += 1
                assigned_stage = stage_count
                stages_end_times.append(end_time)
            else:
                # Update the end time for the assigned stage
                stages_end_times[assigned_stage - 1] = end_time

            # Assign the stage to the current show
            stage_assignments.append((show_name, start_time, end_time, assigned_stage))

        return stage_assignments, stage_count


    def print_schedule(shows):
        """
        Print a schedule table where stages are on the x-axis and hours on the y-axis.

        Parameters:
        shows (list of tuples): A list where each tuple contains the show name, start, and end time.
        """
        # Schedule the shows and get the stage assignments
        scheduled_shows, stages_needed = schedule_shows(shows)

        # Determine the range of hours (y-axis)
        min_time = min(show[1] for show in scheduled_shows)
        max_time = max(show[2] for show in scheduled_shows)

        # Create the schedule matrix
        schedule_matrix = [["" for _ in range(stages_needed)] for _ in range(min_time, max_time + 1)]

        # Fill in the schedule matrix with show names
        for show_name, start_time, end_time, stage in scheduled_shows:
            for hour in range(start_time, end_time + 1):
                schedule_matrix[hour - min_time][stage - 1] = show_name

        # Print the table header
        print(f"{'Hour':<5}", end="")
        for stage in range(1, stages_needed + 1):
            print(f"Stage {stage:<10}", end="")
        print("\n" + "-" * (7 + stages_needed * 12))

        # Print the schedule matrix
        for hour, row in enumerate(schedule_matrix, start=min_time):
            print(f"{hour:<5}", end="")
            for cell in row:
                print(f"{cell:<10}", end="")
            print()


    def read_schedule_from_csv(file_path):
        """
        Read the show schedule from a csv file and return the shows list.

        Parameters:
        file_path (str): The path to the csv file.

        Returns:
        list of tuples: A list where each tuple contains the show name, start, and end time.
        """
        # Read the csv file
        df = pd.read_csv(file_path)

        # Check if required columns are present
        required_columns = ["Show Name", "Start Time", "End Time"]
        for column in required_columns:
            if column not in df.columns:
                raise ValueError(f"Missing required column: {column}")

        # Extract the show name, start time, and end time from the DataFrame
        shows = []
        for _, row in df.iterrows():
            show_name = row["Show Name"]
            start_time = row["Start Time"]
            end_time = row["End Time"]

            # Check if start time and end time are integers
            if not isinstance(start_time, int) or not isinstance(end_time, int):
                raise ValueError(f"Start Time and End Time must be integers. Found: {start_time}, {end_time}")

            # Check if start time is less than end time
            if start_time >= end_time:
                raise ValueError(f"Start Time must be less than End Time. Found: {start_time} >= {end_time}")

            shows.append((show_name, start_time, end_time))

        return shows


    # Save the nicely formatted schedule table to a CSV file
    def save_schedule_to_csv(scheduled_shows, stages_needed, file_path):
        """
        Save the nicely formatted schedule table to a csv file.

        Parameters:
        scheduled_shows (list of tuples): A list where each tuple contains the show name, start time, end time, and assigned stage.
        stages_needed (int): The number of stages needed.
        file_path (str): The path to the csv file.
        """
        # Determine the range of hours (y-axis)
        min_time = min(show[1] for show in scheduled_shows)
        max_time = max(show[2] for show in scheduled_shows)

        # Create the schedule matrix
        schedule_matrix = [["" for _ in range(stages_needed)] for _ in range(min_time, max_time + 1)]

        # Fill in the schedule matrix with show names
        for show_name, start_time, end_time, stage in scheduled_shows:
            for hour in range(start_time, end_time + 1):
                schedule_matrix[hour - min_time][stage - 1] = show_name

        # Create a DataFrame from the schedule matrix
        df = pd.DataFrame(schedule_matrix, columns=[f"Stage {i+1}" for i in range(stages_needed)])
        df.index = range(min_time, max_time + 1)
        df.index.name = "Hour"

        # Save the DataFrame to a csv file
        df.to_csv(file_path)


    shows = read_schedule_from_csv("show_schedule.csv")
    print_schedule(shows)
    save_schedule_to_csv(*schedule_shows(shows), "scheduled_shows.csv") # The * operator is used for unpacking the tuple returned by schedule_shows(shows)
    print_schedule(shows)