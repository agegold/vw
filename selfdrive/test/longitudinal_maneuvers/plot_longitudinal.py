#!/usr/bin/env python3
import os

import matplotlib.pyplot as plt

from common.params import Params
from selfdrive.test.longitudinal_maneuvers.test_longitudinal import maneuvers


if __name__ == "__main__":
  os.environ['SIMULATION'] = "1"
  os.environ['SKIP_FW_QUERY'] = "1"
  os.environ['NO_CAN_TIMEOUT'] = "1"

  params = Params()
  params.clear_all()
  params.put_bool("Passive", bool(os.getenv("PASSIVE")))
  params.put_bool("OpenpilotEnabledToggle", True)
  params.put_bool("ExperimentalMode", False)

#  maneuver_list = (maneuvers[0], maneuvers[1], maneuvers[2])
  maneuver_list = (maneuvers[2], )

  for maneuver in maneuver_list:
    valid, results = maneuver.evaluate()

    ts = []
    v_ego = []
    v_lead = []
    v_rel = []
    a_ego = []
    a_lead = []
    lead_distance = []
    for log_entry in results:
      ts.append(log_entry[0])
      v_ego.append(log_entry[3])
      v_lead.append(log_entry[4])
      a_ego.append(log_entry[5])
      lead_distance.append(log_entry[6])
      v_rel.append(log_entry[7])
      a_lead.append(log_entry[8])

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    ax1.plot(ts, v_lead, "-b", label="lead velocity")
    ax1.plot(ts, v_ego, "-r", label="ego velocity")
    ax1.set(xlabel='time (s)', ylabel='speed (m/s)')
    ax1.legend(loc="upper right")
    ax1.grid()

    ax2.plot(ts, a_lead, "-b", label="lead accel")
    ax2.plot(ts, a_ego, "-r", label="ego accel")
    ax2.set(xlabel='time (s)', ylabel='acceleration (m/s2)')
    ax2.legend(loc="upper right")
    ax2.grid()

    ax3.plot(ts, lead_distance)
    ax3.set(xlabel='time (s)', ylabel='distance (m)')
    ax3.grid()


#    ax4.plot(ts, v_rel)
#    ax4.set(xlabel='time (s)', ylabel='relative speed to lead vehicle (m/s)')
#    ax4.grid()

#    fig.canvas.set_window_title('Test')

  plt.show()
