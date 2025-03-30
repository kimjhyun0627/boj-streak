// https://www.acmicpc.net/problem/13023

import java.util.*
import kotlin.collections.ArrayList
import kotlin.io.*
import kotlin.system.exitProcess

fun dfs(x: Int, level: Int, visited: BooleanArray, friends: Array<ArrayList<Int>>): Boolean {
    if (level == 4) return true

    var res = false
    for (f in friends[x]) {
        if (!visited[f]) {
            visited[f] = true
            if (dfs(f, level + 1, visited, friends)) {
                res = true
                break
            }
            visited[f] = false
        }
    }
    return res
}

fun main() {
    val (N, M) = readLine()!!.split(" ").map { it.toInt() }
    val friends = Array(N) { ArrayList<Int>() }
    repeat(M) {
        val (fr, to) = readLine()!!.split(" ").map { it.toInt() }
        friends[fr].add(to)
        friends[to].add(fr)
    }

    for (ii in friends.indices) {
        if (dfs(ii, 0, BooleanArray(N) { it == ii }, friends)) {
            println(1)
            exitProcess(0)
        }
    }

    println(0)
}
