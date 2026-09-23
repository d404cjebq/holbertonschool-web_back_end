export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  if (weakMap.has(endpoint)) {
    const count = weakMap.get(endpoint) + 1;

    if (count >= 5) {
      throw new Error('Endpoint load is high');
    }

    weakMap.set(endpoint, count);
  } else {
    weakMap.set(endpoint, 1);
  }
}
