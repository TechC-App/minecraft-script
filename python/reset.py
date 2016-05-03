from mcpi import minecraft

RANGE = 64

if __name__ == "__main__":
	mc = minecraft.Minecraft.create()

	mc.setBlocks(-RANGE, -RANGE, -RANGE,
				 RANGE, -1, RANGE, 1)

	mc.setBlocks(-RANGE, -0, -RANGE,
				 RANGE, RANGE, RANGE, 0)

	mc.player.setPos(0.0, 0.0, 0.0)

	mc.postToChat("reset maps and position.")
