// https://www.acmicpc.net/problem/13333

fun main() {
    val N:Int = readln().toInt()
    val indice:MutableList<Int> = readln().split(" ").map { it.toInt() }.toMutableList()
    indice.add(0)
    indice.sortDescending()

    var ans:Int = 0
    for (k in 1..N) {
        if (indice[k - 1] >= k && indice[k] <= k) {
            ans = k
        }
    }

    println(ans)
}

