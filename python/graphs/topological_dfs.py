from dataclasses import dataclass

@dataclass
class Task:
  id: int
  dependencies: list['Task']

  def __hash__(self) -> int:
    return self.id


class GraphHasCycleError(ValueError):
  pass


def topological_sort_dfs(tasks: list[Task]) -> list[Task]:
  """Topologically sort a dependency graph."""
  ordering = []
  todo = set(tasks)
  completed = set()
  inprogress = set()

  def visit(task: Task):
    """Topologically sort the tasks up to and including `task`."""
    # Task is already done; don't need to resolve its dependencies.
    if task.id in completed:
      return

    # We're trying to resolve this task, and it was encountered while
    # recursing through dependencies. This means the task depends on itself.
    if task.id in inprogress:
      raise GraphHasCycleError("The input graph is not a DAG! Unable to create a topological ordering.")

    # Mark that we're working on task.
    inprogress.add(task.id)
    
    # Visit all of the dependencies of task.
    for d in task.dependencies:
      visit(d)

    # Finished resolving dependencies for this task.
    inprogress.remove(task.id)

    # Now that all dependencies have been processed, we can process this task.
    ordering.append(task)

    # Mark that this task is completed.
    completed.add(task.id)

  while len(todo) > 0:
    next_task = todo.pop()
    visit(next_task)

  return ordering


if __name__ == "__main__":
  t0 = Task(0, [])
  t1 = Task(1, [])
  t2 = Task(2, [t0, t1])
  t5 = Task(5, [t2])
  t3 = Task(3, [t2, t5])
  t4 = Task(4, [t3])
  tasks = [t0, t1, t2, t3, t4, t5]
  ordering = topological_sort_dfs(tasks)

  print("Task ordering:")
  for t in ordering:
    print(t.id)