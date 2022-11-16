def grid(maze):
    ''' Maze Properties'''
    num_rows = len(maze)
    num_cols = len(maze[0])
    end_pt = (21, 21)
    start_pt = (0, 0)

    '''BFS'''
    visited = {end_pt: None}
    queue = [end_pt]
    while queue:
        current = queue.pop(0)
        if current == start_pt:
            shortest_path = []
            while current:
                shortest_path.append(current)
                current = visited[current]
            return shortest_path
        adj_points = []
        '''FIND ADJACENT POINTS'''
        current_col, current_row = current
        print(current_col, current_row)

        # Move UP
        if current_row > 0:
            if maze[current_row - 1][current_col] == 0:
                adj_points.append((current_col, current_row - 1))
        # MOVE RIGHT
        if current_col < (len(maze[0])-1):
            if maze[current_row][current_col + 1] == 0:  # There was an error here!
                adj_points.append((current_col + 1, current_row))
        # MOVE DOWN
        if current_row < (len(maze) - 1):
            if maze[current_row + 1][current_col] == 0:
                adj_points.append((current_col, current_row + 1))
        # MOVE LEFT
        if current_col > 0:
            if maze[current_row][current_col - 1] == 0:
                adj_points.append((current_col - 1, current_row))

        '''LOOP THROUGH ADJACENT PTS'''
        for point in adj_points:
            if point not in visited:
                visited[point] = current
                queue.append(point)


