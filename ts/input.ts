export async function lines(): Promise<string[]> {
  const bytes = await Deno.readAll(Deno.stdin);
  const chars = new TextDecoder().decode(bytes);

  return chars.trim().split("\n");
}

export async function numbers(): Promise<number[]> {
  return (await lines())
    .map((value: string) => parseInt(value, 10));
}
