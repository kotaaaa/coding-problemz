function canCompleteCircuit(gas: number[], cost: number[]): number {
  let totalTank = 0;
  let currentTank = 0;
  let startingStation = 0;

  for (let i = 0; i < gas.length; i++) {
    totalTank += gas[i] - cost[i];
    currentTank += gas[i] - cost[i];
    if (currentTank < 0) {
      startingStation = i + 1;
      currentTank = 0;
    }
  }
  return totalTank >= 0 ? startingStation : -1;
}
