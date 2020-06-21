function solve(aWorker) {
    if (aWorker.dizziness === true) {
        aWorker.levelOfHydrated += (0.1 * aWorker.weight) * aWorker.experience;
        aWorker.dizziness = false;
    }
    console.log(aWorker);
    return aWorker;
}

solve({ weight: 80,
        experience: 1,
        levelOfHydrated: 0,
        dizziness: true }
    );
solve({ weight: 120,
        experience: 20,
        levelOfHydrated: 200,
        dizziness: true }
);
solve({ weight: 95,
        experience: 3,
        levelOfHydrated: 0,
        dizziness: false }
    );
