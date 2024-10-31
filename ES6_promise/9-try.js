export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const sum = mathFunction();
    queue.pushsum);
  } catch (TypeError) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
