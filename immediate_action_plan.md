# DARPA Lift Challenge - Immediate Action Plan

## Executive Decision Summary

**RECOMMENDED PATH:** Optimized Octocopter with Hybrid Gas-Electric Power System

**Expected Performance:**
- Aircraft Weight: 35 lbs (15.8 kg)
- Payload Capacity: 240 lbs (109 kg)
- **Payload-to-Weight Ratio: 6.9:1** (73% above competition goal)

**Timeline:** 6-7 months development + 2-3 months testing/optimization
**Budget:** $35,000-45,000 total program cost
**Risk Level:** Medium (manageable with proper execution)

---

## Week 1: Critical Decisions & Setup

### Day 1-2: Team Assembly & Commitment
- [ ] Confirm team members and roles:
  - [ ] Project lead / Systems engineer
  - [ ] Aerodynamics / Structures specialist
  - [ ] Power systems engineer
  - [ ] Controls / Software engineer
  - [ ] Fabrication specialist
  - [ ] Remote pilot (FAA Part 107 certified)

- [ ] Establish communication channels
  - [ ] Weekly meeting schedule
  - [ ] Documentation repository (Google Drive / GitHub)
  - [ ] Real-time communication (Slack / Discord)

- [ ] Secure funding commitment ($40,000-50,000)
  - [ ] Identify funding sources
  - [ ] Create budget proposal
  - [ ] Get approval signatures

### Day 3-4: Design Finalization
- [ ] **DECISION POINT:** Confirm Octocopter vs Quadplane
  - [ ] Review decision matrix
  - [ ] Team vote / consensus
  - [ ] Document decision rationale

- [ ] Create detailed specifications document:
  - [ ] Target weights for each subsystem
  - [ ] Performance requirements
  - [ ] Interface definitions
  - [ ] Test acceptance criteria

### Day 5-7: Procurement Initiation
- [ ] **ORDER IMMEDIATELY (12-week lead time):**
  - [ ] Hybrid power generator (GE70 or equivalent)
    - Vendor: Pegasus Aeronautics or Löweheiser
    - Budget: $3,500-5,000
    - **CRITICAL PATH ITEM**

- [ ] Request quotes for:
  - [ ] Carbon fiber materials (tubing, sheets, cloth)
  - [ ] Brushless motors (8x 600-800W)
  - [ ] Electronic speed controllers (8x 50A+)
  - [ ] Flight controller (Pixhawk Cube Orange)
  - [ ] Propellers (8x 22-24")
  - [ ] LiPo batteries (6S 5000-8000mAh)

- [ ] Setup vendor accounts:
  - [ ] T-Motor or similar (motors/props)
  - [ ] Composite materials supplier
  - [ ] Electronics distributor (DigiKey, etc.)
  - [ ] Amazon / McMaster for hardware

---

## Week 2: Detailed Design

### Structures Design
- [ ] CAD model of complete airframe
  - [ ] Central hub design
  - [ ] Motor mounting arms
  - [ ] Landing gear
  - [ ] Payload attachment system
  - [ ] Fuel tank mounting

- [ ] FEA analysis of critical load paths
  - [ ] Motor arm bending under load
  - [ ] Central hub stress with 240 lb payload
  - [ ] Landing gear impact loads
  - [ ] Safety factor validation (target: 2.0+)

- [ ] Create manufacturing drawings
  - [ ] Carbon fiber layup schedules
  - [ ] Machining specifications
  - [ ] Assembly instructions
  - [ ] Bill of materials

### Power System Design
- [ ] Electrical architecture diagram
  - [ ] Hybrid generator → Battery → ESCs flow
  - [ ] Power distribution board design
  - [ ] Emergency power cutoff
  - [ ] Redundant power paths for critical systems

- [ ] Energy budget validation
  - [ ] Detailed power consumption per flight phase
  - [ ] Battery sizing for peak power
  - [ ] Fuel quantity calculation
  - [ ] Thermal management plan

- [ ] Component specification
  - [ ] Wire gauge selection (ampacity)
  - [ ] Connector types and ratings
  - [ ] Fusing / protection devices
  - [ ] Monitoring sensors (voltage, current, temp)

### Controls Design
- [ ] Flight controller configuration
  - [ ] Octocopter motor layout in firmware
  - [ ] PID tuning plan and baselines
  - [ ] Failsafe behavior definition
  - [ ] Geofence and safety limits

- [ ] Sensor suite specification
  - [ ] GPS (dual redundant)
  - [ ] Barometer (altitude)
  - [ ] IMU (accelerometer, gyro)
  - [ ] Magnetometer (compass)
  - [ ] Airspeed sensor (if applicable)

- [ ] Ground station setup
  - [ ] Telemetry radio selection
  - [ ] Mission Planner / QGroundControl setup
  - [ ] Real-time monitoring displays
  - [ ] Data logging configuration

---

## Month 1: Procurement & Fabrication

### Week 3-4: Component Arrival & Test Rig
- [ ] Receive and inspect initial components
  - [ ] Motors and ESCs
  - [ ] Flight controller and sensors
  - [ ] Electronics and wiring

- [ ] Build power system test stand
  - [ ] Mount motor + prop on load cell
  - [ ] Connect to power meter
  - [ ] Safety shields and emergency stop
  - [ ] Data acquisition system

- [ ] Begin motor/propeller testing
  - [ ] Thrust vs RPM curves
  - [ ] Power consumption measurement
  - [ ] Efficiency optimization
  - [ ] Noise and vibration assessment

- [ ] Start airframe fabrication
  - [ ] Cut carbon fiber tubes for arms
  - [ ] Layup central hub structure
  - [ ] Machine motor mounts
  - [ ] Fabricate landing gear

---

## Month 2: Integration Begins

### Power System Integration
- [ ] **Hybrid generator arrives** (if ordered Week 1)
- [ ] Build hybrid power test rig
  - [ ] Generator mounting fixture
  - [ ] Fuel system (tank, lines, filters)
  - [ ] Battery buffer pack
  - [ ] Load testing capability

- [ ] Bench testing of hybrid system
  - [ ] Startup and shutdown procedures
  - [ ] Power output validation
  - [ ] Fuel consumption measurement
  - [ ] Thermal performance
  - [ ] Runtime testing (30+ minutes)
  - [ ] Safety systems verification

### Airframe Assembly
- [ ] Complete main structure fabrication
- [ ] Install motor mounts (all 8)
- [ ] Mount and wire all motors
- [ ] Install ESCs with cooling
- [ ] Route and protect all wiring
- [ ] Install flight controller
- [ ] Attach landing gear

### Weight Tracking
- [ ] Weigh each component as installed
- [ ] Update weight budget spreadsheet
- [ ] Identify overweight areas
- [ ] Plan weight reduction if needed
- [ ] Verify CG location

---

## Month 3: Ground Testing

### Week 9-10: Tethered Testing
- [ ] Pre-flight safety checks
  - [ ] Propeller security
  - [ ] Motor rotation directions
  - [ ] Control surface responses (N/A for multirotor)
  - [ ] Emergency stop function
  - [ ] Tether strength verification

- [ ] Low-power tethered tests
  - [ ] 25% throttle hover attempt
  - [ ] Control response validation
  - [ ] Vibration assessment
  - [ ] Initial PID tuning

- [ ] Full-power tethered tests
  - [ ] Hover with no payload
  - [ ] Hover with incremental payload (50, 100, 150, 200 lbs)
  - [ ] Maximum thrust test
  - [ ] Sustained hover endurance

### Week 11-12: Control System Tuning
- [ ] PID tuning (no payload)
  - [ ] Roll axis
  - [ ] Pitch axis
  - [ ] Yaw axis
  - [ ] Altitude hold

- [ ] PID tuning (with payload)
  - [ ] Repeat for 150 lb payload
  - [ ] Repeat for 240 lb payload
  - [ ] Save multiple configurations

- [ ] Autonomous mode testing
  - [ ] GPS hold
  - [ ] Waypoint navigation (tethered)
  - [ ] Altitude hold accuracy
  - [ ] Return-to-launch function

---

## Month 4: First Flights

### Week 13-14: Hover Flight Tests (No Payload)
- [ ] **GO/NO-GO REVIEW:** Readiness for first flight
  - [ ] All systems functional
  - [ ] Weight budget confirmed
  - [ ] Safety procedures reviewed
  - [ ] Remote pilot briefed
  - [ ] Test site approved
  - [ ] Insurance / waivers current

- [ ] First free flight (HOVER ONLY)
  - [ ] 3-5 ft altitude, 30 seconds
  - [ ] Gradual altitude increase to 20 ft
  - [ ] Extended hover (5-10 minutes)
  - [ ] Controlled landing practice

- [ ] Basic maneuvering
  - [ ] Forward/backward translation
  - [ ] Left/right translation
  - [ ] Yaw rotations
  - [ ] Figure-8 patterns

### Week 15-16: Payload Flight Tests
- [ ] Incremental payload testing
  - [ ] 50 lb payload hover
  - [ ] 100 lb payload hover
  - [ ] 150 lb payload hover
  - [ ] 200 lb payload hover
  - [ ] 240 lb payload hover (MAX)

- [ ] Performance data collection
  - [ ] Hover power at each weight
  - [ ] Control authority assessment
  - [ ] Vibration and stability
  - [ ] Battery/fuel consumption

- [ ] Payload release mechanism testing
  - [ ] Ground tests (100 cycles)
  - [ ] Hover release tests
  - [ ] Emergency release function

---

## Month 5: Mission Profile Testing

### Week 17-18: Distance Flights (Unloaded)
- [ ] Short distance flights
  - [ ] 0.5 nm at 350 ft AGL
  - [ ] 1.0 nm at 350 ft AGL
  - [ ] 2.0 nm at 350 ft AGL

- [ ] Speed optimization
  - [ ] Test at 20, 25, 30 km/h
  - [ ] Measure power consumption
  - [ ] Determine most efficient cruise speed
  - [ ] Wind sensitivity assessment

- [ ] Altitude hold validation
  - [ ] 350 ft ± 50 ft compliance
  - [ ] GPS altitude vs barometric
  - [ ] AGL vs MSL awareness

### Week 19-20: Full Mission Rehearsals (Loaded)
- [ ] 4 nm loaded flight
  - [ ] 150 lb payload first
  - [ ] 200 lb payload second
  - [ ] 240 lb payload third
  - [ ] Monitor time and energy closely

- [ ] Complete mission profile
  - [ ] Takeoff with 240 lb payload
  - [ ] Cruise 4 nm at 350 ft AGL
  - [ ] Land and release payload
  - [ ] Takeoff unloaded
  - [ ] Cruise 1 nm at 350 ft AGL
  - [ ] Land in 10 ft circle
  - [ ] **TARGET: Under 25 minutes**

- [ ] Data analysis
  - [ ] Actual vs predicted energy use
  - [ ] Time breakdown by phase
  - [ ] Margin assessment
  - [ ] Identify optimization opportunities

---

## Month 6-7: Optimization & Reliability

### Performance Optimization
- [ ] Weight reduction efforts
  - [ ] Identify non-essential components
  - [ ] Replace heavy items with lighter alternatives
  - [ ] Optimize structures (machining lightening holes, etc.)
  - [ ] **TARGET: Get to 30-32 lbs if possible**

- [ ] Aerodynamic cleanup
  - [ ] Streamline wiring
  - [ ] Add minimal fairings if beneficial
  - [ ] Propeller optimization (pitch, diameter)

- [ ] Energy optimization
  - [ ] Tune cruise speed for minimum power
  - [ ] Optimize climb rate
  - [ ] Refine PID gains for efficiency

### Reliability Testing
- [ ] Endurance testing
  - [ ] 10x full mission profiles
  - [ ] Component wear inspection
  - [ ] Failure mode discovery
  - [ ] Mean time between failures

- [ ] Environmental testing
  - [ ] Hot weather (95°F+)
  - [ ] Cold weather (40°F)
  - [ ] Windy conditions (15-25 kt)
  - [ ] Different altitudes (if possible)

- [ ] Worst-case scenarios
  - [ ] Single motor failure (can it land?)
  - [ ] GPS loss (manual control)
  - [ ] Telemetry loss (pre-programmed mission)
  - [ ] Low fuel / battery

### Build Backup Aircraft
- [ ] Order second set of components
- [ ] Replicate successful design
- [ ] Independent assembly and testing
- [ ] Maintain as hot spare

---

## Month 8: Pre-Competition Prep

### Documentation & Compliance
- [ ] Competition registration (by May 1, 2026)
  - [ ] Team information
  - [ ] Aircraft specifications
  - [ ] Weight declarations
  - [ ] Preliminary flight window preferences

- [ ] FAA compliance
  - [ ] Part 107 certificates current
  - [ ] Remote ID module installed and tested
  - [ ] Waivers if needed (multi-aircraft, etc.)
  - [ ] Insurance documentation

- [ ] Technical documentation
  - [ ] Flight manual / procedures
  - [ ] Maintenance logs
  - [ ] Component specifications
  - [ ] Test results summary
  - [ ] Safety analysis

### Competition Strategy
- [ ] Flight window selection
  - [ ] Weather forecast monitoring
  - [ ] Time of day preferences (winds)
  - [ ] Backup window strategy

- [ ] Maximum payload determination
  - [ ] Incremental testing to find absolute max
  - [ ] Safety margin definition
  - [ ] Competition payload selection (conservative vs aggressive)

- [ ] Time optimization
  - [ ] Minimize ground time
  - [ ] Optimize climb/descent rates
  - [ ] Perfect landing approach
  - [ ] Payload release efficiency

### Pilot Training
- [ ] Competition scenario practice
  - [ ] Pressure and stress management
  - [ ] Backup pilot qualification
  - [ ] Emergency procedures refresher
  - [ ] Course familiarization (if possible)

- [ ] Equipment familiarization
  - [ ] DARPA-provided tracker installation practice
  - [ ] Weigh-in procedure practice
  - [ ] Rapid turnaround between attempts

---

## Month 9-10: Final Prep & Competition

### Transport & Logistics
- [ ] Packing plan
  - [ ] Aircraft disassembly procedure
  - [ ] Protective cases and foam
  - [ ] Spare parts inventory
  - [ ] Tools and test equipment
  - [ ] Fuel and batteries (shipping regulations!)

- [ ] Travel arrangements
  - [ ] Team transportation
  - [ ] Lodging near competition site
  - [ ] Rental vehicle (cargo capacity)
  - [ ] Schedule with buffer days

### On-Site Preparation
- [ ] Setup and systems check
  - [ ] Reassemble aircraft
  - [ ] Function tests
  - [ ] Weight verification (unofficial)
  - [ ] Course reconnaissance
  - [ ] Weather monitoring

- [ ] Final optimization
  - [ ] Adjust for local conditions (altitude, temperature)
  - [ ] Last-minute PID tweaks if needed
  - [ ] Fuel mixture adjustment
  - [ ] Practice flights if allowed

### Competition Execution
- [ ] Window 1 (Day 1)
  - [ ] Conservative first attempt (200 lb payload)
  - [ ] If successful, increase payload
  - [ ] Multiple attempts if time allows
  - [ ] Data collection for optimization

- [ ] Analysis between windows
  - [ ] Review telemetry data
  - [ ] Identify improvements
  - [ ] Adjust strategy for Window 2

- [ ] Window 2 (Day 2)
  - [ ] Implement optimizations
  - [ ] Maximum payload attempt
  - [ ] Multiple runs for best score
  - [ ] **Target: 240 lb payload, 6.9:1 ratio**

---

## Critical Success Factors

### Top 5 Priorities (In Order)
1. **Hybrid Power System Delivery** - Order immediately, 12-week lead time
2. **Weight Budget Discipline** - Track every gram, stay under 35 lbs
3. **Thorough Testing** - 20+ full mission profiles before competition
4. **Backup Aircraft** - Redundancy is insurance against failure
5. **Team Coordination** - Clear roles, communication, decision-making

### Key Metrics to Track
- **Weight:** Current vs budget (weekly updates)
- **Power:** Measured vs predicted (every test)
- **Time:** Mission duration (target <25 min, limit 30 min)
- **Reliability:** Success rate of mission attempts (target >90%)
- **Payload Ratio:** Ongoing calculation as design evolves

### Decision Gates
- **End of Month 1:** Design frozen, fabrication complete
- **End of Month 3:** First flight successful
- **End of Month 5:** Full mission profile achieved
- **End of Month 7:** Reliability demonstrated (10x missions)
- **Month 8:** GO/NO-GO for competition entry

### Risk Mitigation
- **Schedule Risk:** Start early, parallel work streams
- **Technical Risk:** Conservative design choices, proven components
- **Financial Risk:** Secure funding upfront, 20% contingency
- **Regulatory Risk:** Early FAA engagement, compliance by design
- **Competition Risk:** Backup aircraft, multiple attempts strategy

---

## Immediate Next Steps (This Week!)

### Monday
- [ ] Team meeting: Review this document
- [ ] Assign roles and responsibilities
- [ ] Create project management system (Trello, Asana, etc.)

### Tuesday
- [ ] Final design decision: Octocopter vs Quadplane
- [ ] Begin CAD modeling
- [ ] Research hybrid generator vendors

### Wednesday
- [ ] **CRITICAL:** Place order for hybrid power generator
- [ ] Request quotes for motors, ESCs, props
- [ ] Request quotes for carbon fiber materials

### Thursday
- [ ] Finalize detailed specification document
- [ ] Create component spreadsheet with vendors and prices
- [ ] Setup budget tracking system

### Friday
- [ ] Team review of week's progress
- [ ] Place additional component orders
- [ ] Schedule Week 2 activities
- [ ] Document decisions and rationale

---

## Resources & Contacts

### Hybrid Generator Vendors
- **Pegasus Aeronautics** (GE70): https://www.pegasusaero.ca/
- **Löweheiser**: https://www.loweheiser.com/
- **Foxtech** (NOVA series): https://www.foxtechfpv.com/

### Motor/Propeller Vendors
- **T-Motor**: https://store.tmotor.com/
- **KDE Direct**: https://www.kdedirect.com/
- **MAD Components**: https://www.madcomponents.co.uk/

### Electronics
- **Pixhawk**: https://pixhawk.org/
- **ArduPilot**: https://ardupilot.org/
- **DigiKey**: https://www.digikey.com/

### Materials
- **Composite materials:** DragonPlate, CST Composites, ACP Composites
- **Hardware:** McMaster-Carr, Bolt Depot
- **Batteries:** Tattu, Gens Ace

### Competition
- **DARPA Lift Challenge**: https://www.darpa.mil/research/challenges/lift
- **Rules**: (provided in original document)
- **Contact**: darpaliftchallenge@darpa.mil
- **Registration Opens**: January 5, 2026
- **Feedback Deadline**: November 26, 2025 (send rule feedback!)

---

## Budget Tracker Template

| Category | Budgeted | Actual | Variance | Notes |
|----------|----------|--------|----------|-------|
| Hybrid Power | $4,500 | | | |
| Motors/ESCs | $1,500 | | | |
| Props | $300 | | | |
| Flight Controller | $1,000 | | | |
| Carbon Fiber | $2,000 | | | |
| Electronics | $800 | | | |
| Batteries | $500 | | | |
| Hardware | $400 | | | |
| Test Equipment | $1,500 | | | |
| Backup Aircraft | $12,000 | | | |
| Spares | $3,000 | | | |
| Travel | $3,000 | | | |
| Contingency | $7,000 | | | |
| **TOTAL** | **$37,500** | | | |

---

## Contact Information Template

| Role | Name | Email | Phone | Backup |
|------|------|-------|-------|--------|
| Team Lead | | | | |
| Structures | | | | |
| Power Systems | | | | |
| Controls | | | | |
| Fabrication | | | | |
| Remote Pilot | | | | |
| Backup Pilot | | | | |

---

**Document Status:** READY FOR EXECUTION
**Next Review Date:** [Fill in after team meeting]
**Decision Deadline:** December 15, 2025
**Competition Registration:** January 5, 2026
**Competition Date:** Summer 2026

**LET'S BUILD A WINNER!** 🚁
