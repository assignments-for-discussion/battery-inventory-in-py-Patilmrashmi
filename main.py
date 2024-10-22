def count_batteries_by_health(present_capacities):
  rated_capacity = 120 # represents the rated capacity of a battery.
  # health_counts is the dictionary to store the count of each health category
  health_counts = {
        "healthy": 0,    # Count for healthy batteries whose SoH > 83%
        "exchange": 0,   # Count for batteries that need to be exchanged.Thier soh lies range of (63% ,83%] 
        "failed": 0      # Count for failed batteries (SoH less than or equal to 63%)
    }

      # Loop through each present capacity to calculate SoH and classify
  for present_capacity in present_capacities:         
        # Here we calculate State of Health (SoH) in percentage
        soh = 100 * present_capacity / rated_capacity
        
        # Classify based on SoH and update counts accordingly
        if soh > 83:
            health_counts["healthy"] += 1
        elif 63 < soh <= 83:
            health_counts["exchange"] += 1
        else:
            health_counts["failed"] += 1
  return health_counts


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [113, 116, 80, 95, 92, 70]  #present_capacities is a list that stores the current capacities of batteries
  counts = count_batteries_by_health(present_capacities) # Get the total count of batteries
  # Asserts is used to verify if the counts matches the expected value
  assert(counts["healthy"] == 2)  # 113, 116 are  healthy
  assert(counts["exchange"] == 3) # 80, 95, 92 should be exchange
  assert(counts["failed"] == 1)   # 70 should be failed
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
