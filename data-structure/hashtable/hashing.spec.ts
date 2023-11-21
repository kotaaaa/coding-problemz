import { Hashing } from "./hashing";
import { datas } from "./data";

const hashing = new Hashing();

for (let i = 0; i < datas.length; i++) {
  if (datas[i].action === "insert") {
    hashing.insert(datas[i].val);
  } else {
    if (hashing.find(datas[i].val) >= 0) {
      console.log("yes");
    } else {
      console.log("no");
    }
  }
}
