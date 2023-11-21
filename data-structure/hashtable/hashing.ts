export class Hashing {
  M: number = 1046527;
  H: string[] = Array.from({ length: this.M }, () => "");

  getChar(ch: string) {
    if (ch === "A") {
      return 1;
    } else if (ch === "C") {
      return 2;
    } else if (ch === "G") {
      return 3;
    } else if (ch === "T") {
      return 4;
    } else {
      return 0;
    }
  }

  getKey(str: string): number {
    let sum = 0;
    let p = 1;
    for (let i = 0; i < str.length; i++) {
      sum += p * this.getChar(str[i]);
      p *= 5;
    }
    return sum;
  }

  h1(key: number): number {
    return key % this.M;
  }
  h2(key: number): number {
    return 1 + (key % (this.M - 1));
  }

  find(str: string): number {
    let key: number = this.getKey(str);
    for (let i = 0; i < this.M; i++) {
      let h = (this.h1(key) + i * this.h2(key)) % this.M;
      if (this.H[h] === str) {
        return h; // Key found
      } else if (this.H[h] === "" || this.H[h] === undefined) {
        return -1; // Empty slot found
      }
    }
    return -1;
  }

  insert(str: string): number {
    let key: number = this.getKey(str);
    for (let i = 0; i < this.M; i++) {
      let h = (this.h1(key) + i * this.h2(key)) % this.M;
      if (this.H[h] === str) {
        return h; // Key found
      } else if (this.H[h] === "" || this.H[h] === undefined) {
        this.H[h] = str;
        return 0;
      }
    }
    return -1;
  }
}
