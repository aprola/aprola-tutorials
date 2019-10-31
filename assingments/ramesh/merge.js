'use-strict';
function mergeSort (sample) {
    if (sample.length === 1) {
      return sample;
    }
    const middle = Math.floor(sample.length / 2);
    const left = sample.slice(0, middle);
    const right = sample.slice(middle);
    return merge(
      mergeSort(left),
      mergeSort(right)
    );
  }
  
  function merge (left, right) {
    let result = [];
    let indexLeft = 0;
    let indexRight = 0;
    while (indexLeft < left.length && indexRight < right.length) {
      if (left[indexLeft] < right[indexRight]) {
        result.push(left[indexLeft]);
        indexLeft++;
      } else {
        result.push(right[indexRight]);
        indexRight++;
      }
    }
    return result.concat(left.slice(indexLeft)).concat(right.slice(indexRight));
  }
  
  const list = [2, 5, 1, 3, 7, 2, 3, 8, 6, 3];
  console.log(mergeSort(list));