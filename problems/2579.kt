import java.io.BufferedReader
import java.io.InputStreamReader

fun main() {
    val br = BufferedReader(InputStreamReader(System.`in`))

    val n = br.readLine().trim().toInt()
    val stairs = IntArray(n+1)
    for (ii in 1 until n+1) {
        stairs[ii] = br.readLine().trim().toInt()
    }

    if (n == 1) {
        println(stairs[1])
        return
    }

    val dp = IntArray(n+1)

    for (ii in 1 until n+1) {
        when (ii) {
            1 -> dp[1] = stairs[1]
            2 -> dp[2] = maxOf(stairs[1] + stairs[2], stairs[2])
            else -> dp[ii] = maxOf(
                dp[ii - 3] + stairs[ii - 1] + stairs[ii],
                dp[ii - 2] + stairs[ii]
            )
        }
    }

    println(dp[n])
}