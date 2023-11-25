import { PriorityQueue } from "./priorityQueue";
import { datas } from "./data";

let priorityQueue: PriorityQueue = new PriorityQueue();
for (let i = 0; i < datas.length; i++) {
  if (datas[i].action === "insert") {
    priorityQueue.insert(datas[i].val!);
  } else {
    console.log(priorityQueue.extract());
  }
}
