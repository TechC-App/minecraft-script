# -*- coding: utf-8 -*-
# サンプル - 宝探し -

from mcpi import minecraft
from mcpi import block
import time
import random
import math

# 指定された座標を整数値に丸めたものを返す
def roundVec3(vec3):
	return minecraft.Vec3(int(vec3.x), int(vec3.y), int(vec3.z))

# 指定された座標を中心にランダムな座標を生成して返す
def randomVec3(vec3):
	x = random.randrange(vec3.x - 50, vec3.x + 50)
	y = random.randrange(vec3.y -  5, vec3.y +  5)
	z = random.randrange(vec3.z - 50, vec3.z + 50)
	return minecraft.Vec3(x, y, z)

# 指定した2点間の距離を返す
def distance(point1, point2):
	xd = point2.x - point1.x
	yd = point2.y - point1.y
	zd = point2.z - point1.z
	return math.sqrt(xd**2 + yd**2 + zd**2)

# メイン処理
if __name__ == "__main__":
	# 初期化
	mc = minecraft.Minecraft.create()

	# プレイヤーの現在値を整数値で取得
	playerPos = roundVec3(mc.player.getPos())

	# ランダムな場所にダイヤモンドブロックを配置
	randomBlockPos = randomVec3(playerPos)
	mc.setBlock(randomBlockPos.x, randomBlockPos.y, randomBlockPos.z, block.DIAMOND_BLOCK)
	mc.postToChat("Hide a treasure somewhere. Please look for it !!")
 
	lastDist = distance(randomBlockPos, playerPos)
	startedTime = time.time()

	# お宝が見つかるまで以下処理をループ
	while True:
		# お宝との距離をチェック
		dist = distance(randomBlockPos, mc.player.getPos())
		if dist < 2:
			# 隣のマスまで近づいていれば見つけたとする
			break
		else:
			# お宝までの距離を表示
			if dist < lastDist:
				mc.postToChat("The treasure is nearer to you !! " + str(int(dist)) + " blocks away.")
			if dist > lastDist:
				mc.postToChat("The treasure is far from you ... " + str(int(dist)) + " blocks away.")
	 
		lastDist = dist
		time.sleep(1)

	# お宝が見つかったら、経過時間と共にメッセージ表示
	mc.postToChat("Congratulations !! You find the treasure. "
		+ str(int(time.time() - startedTime))
		+ "seconds to find.")
