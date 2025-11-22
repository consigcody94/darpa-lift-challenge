# DARPA Lift Challenge - Research & Strategy

## Overview

This directory contains comprehensive research and strategic planning for the **DARPA Lift Challenge** (Summer 2026), a $6.5M competition to develop VTOL drones capable of carrying payloads 4+ times their own weight.

## Competition Quick Facts

- **Aircraft weight limit:** < 55 lbs
- **Minimum payload:** 110 lbs (to qualify for scoring)
- **Mission:** 5 nautical miles (4 nm loaded + 1 nm unloaded)
- **Time limit:** 30 minutes
- **Altitude:** 350 ft AGL (±50 ft)
- **Scoring metric:** Payload weight ÷ Aircraft weight (higher = better)
- **Prize pool:** $6.5M total
  - 1st place: $2.5M
  - 2nd place: $1.5M
  - 3rd place: $1.0M
  - 3x bonus prizes: $500K each (aerodynamics, powertrain, most promising)

## Documents in This Repository

### 1. `darpa_lift_challenge_analysis.md` - COMPREHENSIVE TECHNICAL ANALYSIS
**The deep-dive technical document.** Contains:
- Detailed mission requirements and calculations
- Power system analysis (battery vs gas vs hybrid)
- Complete design architecture comparison
- Energy and weight budget calculations
- Risk analysis
- 10-month development roadmap
- Budget estimates ($36K-59K)
- Component recommendations
- Technical references

**Read this for:** Technical depth, engineering calculations, design justification

### 2. `design_decision_matrix.md` - DECISION FRAMEWORK
**The strategic comparison tool.** Contains:
- Scored comparison of top 3 designs (quadplane, octocopter, tiltrotor)
- Head-to-head analysis with detailed metrics
- Final recommendation with rationale
- Success probability estimates
- Go/No-Go decision criteria

**Read this for:** Quick decision-making, design trade-offs, strategic direction

### 3. `immediate_action_plan.md` - EXECUTION PLAYBOOK
**The week-by-week implementation guide.** Contains:
- Day-by-day actions for first week
- Month-by-month development plan
- Critical path items and procurement
- Testing and validation procedures
- Competition preparation checklist
- Budget tracker templates
- Contact information templates

**Read this for:** What to do RIGHT NOW, project management, timeline

### 4. `README.md` - THIS FILE
**The navigation guide and executive summary.**

---

## Executive Summary

### RECOMMENDED SOLUTION: Optimized Octocopter with Hybrid Gas-Electric Power

#### Why This Design Wins

**Performance:**
- Aircraft weight: **35 lbs** (15.8 kg)
- Payload capacity: **240 lbs** (109 kg)
- **Payload-to-weight ratio: 6.9:1**
- This is **73% better** than the stated competition goal of 4:1
- Likely to be **top-tier performance**

**Feasibility:**
- Lower technical risk than hybrid VTOL (no transition phase)
- Proven multirotor control algorithms
- Faster development time (6-7 months vs 9-10 months)
- Simpler design = fewer failure modes

**Innovation:**
- Hybrid gas-electric power at this scale is novel
- Ultra-lightweight carbon fiber construction
- Low disk loading for efficiency
- Eligible for "Revolutionary Powertrain" bonus prize ($500K)

#### Key Design Features

**Configuration:**
- 8 brushless motors (coaxial, 4 arms)
- 22-24" propellers for low disk loading
- Hybrid generator: 4-6 kW continuous power
- Small LiPo buffer battery for power spikes
- Minimal carbon fiber frame structure

**Power System (The Game-Changer):**
- Gasoline has **50x the energy density** of batteries
- Hybrid generator weighs only **7.5 kg** (16.5 lbs)
- Provides **4,000+ Wh** of energy (vs 2,920 Wh needed)
- Battery-only system would require **22-28 lbs** just for batteries!
- **This is what makes the 6.9:1 ratio possible**

**Weight Budget:**
- Frame/structure: 2.0 kg (4.4 lbs)
- 8 motors + controllers: 4.0 kg (8.8 lbs)
- Hybrid power system: 7.5 kg (16.5 lbs)
- Landing gear: 1.0 kg (2.2 lbs)
- Electronics/sensors: 0.8 kg (1.8 lbs)
- Payload mount: 0.5 kg (1.1 lbs)
- **Total: 15.8 kg (34.8 lbs)**
- **Margin to 55 lb limit: 20.2 lbs** ✅

#### Alternative Design: Quadplane Hybrid VTOL

If the team has strong aerodynamics expertise and needs the efficiency:

**Configuration:** Fixed wing + 4 lift motors + pusher prop + hybrid power

**Performance:**
- Aircraft weight: 45 lbs
- Payload capacity: 220 lbs
- Ratio: 4.9:1 (still very competitive)
- 30-40% more energy efficient than octocopter

**Trade-offs:**
- More complex (transition flight phase)
- Longer development time (9-10 months)
- Eligible for multiple bonus prizes (aerodynamics + powertrain)
- Lower payload ratio but higher innovation factor

**Choose this if:**
- Team has aerospace/aerodynamics background
- Full 10-month timeline available
- Want to compete for multiple prize categories
- Prioritize efficiency and innovation

---

## Critical Success Factors

### The 5 Most Important Things

1. **ORDER HYBRID GENERATOR IMMEDIATELY**
   - 12-week lead time - this is the critical path
   - Recommended: GE70 (3.5 kg, 4kW) from Pegasus Aeronautics
   - Cost: ~$4,000-5,000

2. **Obsessive Weight Management**
   - Weigh every component
   - Track against budget weekly
   - Target 30-35 lbs to maximize payload margin

3. **Extensive Testing**
   - Minimum 20 full mission profiles before competition
   - Test with maximum payload repeatedly
   - Validate reliability >90% success rate

4. **Build a Backup Aircraft**
   - Mechanical failures happen
   - Insurance against catastrophic failure
   - Use same design, independent build

5. **Team Coordination & Expertise**
   - Need: structures, power systems, controls, pilot
   - Clear roles and decision authority
   - Regular communication and documentation

---

## Timeline & Budget

### Development Timeline
- **Months 1-2:** Design finalization, procurement
- **Month 3:** Fabrication and ground testing
- **Months 4-5:** Flight testing (no payload → full payload)
- **Months 6-7:** Mission profile testing and optimization
- **Month 8:** Reliability testing and backup aircraft
- **Months 9-10:** Competition prep and final validation

**Total: 9-10 months** (Octocopter can be 2-3 months faster)

### Budget Summary
- **Component costs:** $18,000-27,000 (two aircraft)
- **Development/testing:** $5,000-10,000
- **Tools and equipment:** $2,000-3,000
- **Spares:** $3,000-5,000
- **Travel:** $2,000-4,000
- **Contingency (20%):** $6,000-10,000
- **Total: $36,000-59,000**

**Expected ROI:** 2,000% - 6,000% if competitive

---

## Immediate Next Steps

### This Week (Week 1):

**Monday:**
- Assemble team
- Assign roles
- Review all documentation

**Tuesday:**
- Final decision: Octocopter or Quadplane
- Begin CAD modeling
- Identify hybrid generator vendors

**Wednesday:** ⚠️ **CRITICAL**
- **PLACE ORDER for hybrid generator** (12-week lead time!)
- Request quotes for motors, ESCs, propellers
- Request quotes for carbon fiber materials

**Thursday:**
- Finalize specifications
- Create budget tracking system
- Setup project management tools

**Friday:**
- Review week's progress
- Place remaining component orders
- Plan Month 1 activities

### Decision Deadline
**Must commit by:** December 15, 2025 (to meet development timeline)

### Key Dates
- **Feedback on draft rules:** November 26, 2025
- **Registration opens:** January 5, 2026
- **Registration closes:** May 1, 2026
- **Competition:** Summer 2026

---

## Risk Assessment

### Technical Risks: MEDIUM
- Power system integration: LOW (proven technology)
- Weight budget: MEDIUM (requires discipline)
- Flight stability with heavy payload: MEDIUM (requires tuning)
- Mission completion: MEDIUM (energy margins are adequate)

### Schedule Risks: MEDIUM-LOW
- Hybrid generator lead time: HIGH (mitigated by immediate order)
- Flight testing weather: MEDIUM (plan for delays)
- Component availability: LOW (commercial off-the-shelf)

### Financial Risks: LOW
- Budget is reasonable for complexity
- Prize money provides strong incentive
- Incremental spending reduces risk

### Competition Risks: MEDIUM
- Other teams may achieve higher ratios: MEDIUM
- Weather during competition: MEDIUM
- Mechanical failure: MEDIUM (mitigated by backup aircraft)

**Overall Risk: MEDIUM - Manageable with proper execution**

---

## Success Probability Estimates

### Octocopter Design:
- Complete mission successfully: **80%**
- Achieve 5:1+ ratio: **70%**
- Place in top 3: **40%**
- Win 1st place: **15%**
- Win bonus prize: **20%**

### Quadplane Design:
- Complete mission successfully: **65%**
- Achieve 4.5:1+ ratio: **60%**
- Place in top 3: **35%**
- Win 1st place: **12%**
- Win bonus prizes: **25%** (multiple categories)

---

## Key Insights from Research

### 1. Power System is Everything
- Batteries alone: Not viable for competitive ratios (too heavy)
- Gasoline has 50x energy density advantage
- Hybrid system is the only way to achieve 4:1+ ratio
- This is the single most important design decision

### 2. Weight Discipline Wins
- Every pound of aircraft weight costs 4-7 lbs of payload
- Carbon fiber construction is mandatory
- Conservative 35 lb aircraft → 240 lb payload = 6.9:1 ratio
- Aggressive 30 lb aircraft → 280 lb payload = 9.3:1 ratio!

### 3. Simplicity Has Value
- Octocopter: Simpler but heavier power system needed
- Quadplane: More efficient but more complex
- Trade-off is close - choose based on team expertise

### 4. The Mission Profile Matters
- Only 5 nm = relatively short distance
- 30 minute limit = not endurance-focused
- Scoring is pure payload ratio, not efficiency
- This favors lighter aircraft over efficient aircraft

### 5. Testing is Non-Negotiable
- Need 20+ successful mission profiles
- Reliability testing will uncover issues
- Backup aircraft is mandatory
- Practice makes perfect for competition

---

## Regulatory Compliance

### FAA Requirements (Built Into Design):
- ✅ Part 107 remote pilot certificate required
- ✅ Remote ID module (required by FAA)
- ✅ Visual line of sight (VLOS) operation
- ✅ Under 55 lbs aircraft weight (Part 107 limit)
- ⚠️ May need waiver for operations with hybrid gasoline system

### Safety Considerations:
- Redundant flight controllers and GPS
- Emergency power cutoff systems
- Fail-safe return-to-launch
- Geofencing and altitude limits
- Tether testing before free flight

---

## Questions & Answers

### Q: Why not use hydrogen fuel cells?
A: Hydrogen systems have better energy density but are immature, expensive, and heavy. Gasoline hybrid is proven and commercially available now.

### Q: Could we achieve 10:1 ratio?
A: Theoretically yes, with a 25 lb aircraft and 250 lb payload. But risk is very high - structural limits, control challenges, and power requirements become extreme.

### Q: What if the hybrid generator fails?
A: Buffer battery provides emergency power for controlled landing. This is a critical safety feature.

### Q: Can we use lighter-than-air assistance?
A: No - explicitly forbidden in rules (Section 2.7).

### Q: What's the biggest risk?
A: Honestly, it's getting the hybrid generator on time. Order it IMMEDIATELY. Second is exceeding weight budget - requires constant vigilance.

---

## Conclusion

**The DARPA Lift Challenge is winnable with current technology.**

The key insight: **Hybrid gas-electric power systems unlock payload ratios that are impossible with batteries alone.**

By combining:
- Ultra-lightweight carbon fiber construction
- Hybrid power system (50x better energy density)
- Low disk loading for efficiency
- Proven multirotor control

We can achieve a **6.9:1 payload-to-weight ratio** with the octocopter design, or a **4.9:1 ratio** with more efficient quadplane design.

Both are highly competitive. The choice depends on team expertise and timeline.

**The path forward is clear. The technology exists. The prize is significant.**

**Now it's time to build.**

---

## Document Change Log

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| Nov 22, 2025 | 1.0 | Initial research and analysis | Claude |

---

## Contact & Support

**DARPA Lift Challenge:**
- Website: https://www.darpa.mil/research/challenges/lift
- Email: darpaliftchallenge@darpa.mil
- Rules feedback deadline: November 26, 2025

**For questions about this research:**
- Review the three detailed documents first
- All calculations and assumptions are documented
- Sources are cited throughout

---

**Ready to compete? Let's revolutionize heavy-lift VTOL technology.** 🚁🏆
