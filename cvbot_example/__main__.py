import asyncio
import os

from cvbot.communication.txtapiclient import TxtApiClient
from cvbot.config.drive_robot_configuration import DriveRobotConfiguration
from cvbot.controller.easy_drive_controller import EasyDriveController
import numpy as np


async def main() -> None:
    host = os.getenv("TXT_API_HOST", "localhost")
    port = int(os.getenv("TXT_API_PORT", 8080))
    key = os.getenv("TXT_API_KEY", None)

    client = TxtApiClient(host, port, key)
    await client.initialize()
    drive_controller = EasyDriveController(client, DriveRobotConfiguration())

    await drive_controller.drive(np.array([0.0, 500.0, 1000.0]))
    await asyncio.sleep(50)
    await drive_controller.stop()


if __name__ == "__main__":
    asyncio.run(main())
