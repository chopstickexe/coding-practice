from typing import Any, List


class UnionFind:
    def __init__(self, values: List[Any]) -> None:
        self.v2x = {}
        self.x2v = {}
        for i, v in enumerate(values):
            self.v2x[v] = i
            self.x2v[i] = v

        self.N = len(values)

        self.par = [i for i in range(self.N)]
        self.rank = [0 for _ in range(self.N)]

    def find(self, v: Any) -> Any:
        x = self.v2x[v]
        y = self._find(x)
        return self.x2v[y]

    def _find(self, x: int) -> int:
        if self.par[x] == x:
            # This is the root
            return x
        else:
            # Find the root and memorize
            self.par[x] = self._find(self.par[x])
            return self.par[x]

    def unite(self, vx: Any, vy: Any) -> None:
        x = self.v2x[vx]
        y = self.v2x[vy]
        self._unite(x, y)

    def _unite(self, x: int, y: int) -> None:
        x = self._find(x)
        y = self._find(y)
        if x == y:
            # Already united
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same(self, vx: Any, vy: Any) -> bool:
        return self._same(self.v2x[vx], self.v2x[vy])

    def _same(self, x: int, y: int) -> bool:
        return self._find(x) == self._find(y)
